import os
import tempfile
import shutil
from data import EncryptedFileTree
from .encryption import Encrypt
from django.db.models import Q
from functions import get_name_from_path, get_encryption_key


class Vault:
    def __init__(self, user) -> None:
        self.user = user

    def get_initials(self):
        return self.get_children(fileTree=None)

    def delete_temp(self) -> bool:
        """
        This method will delete every temporary files that the app have used, like, temporary decrypted file.
        """
        return False

    def get_children(self, fileTree):
        # if it is image then send the content by decrypting too! call get_decrypted()
        initial_files = EncryptedFileTree.objects.filter(
            Q(parent_directory=fileTree) & Q(owner=self.user))
        # TODO send thumbnail for image file
        return initial_files

    def get_voice(self):
        initial_files = EncryptedFileTree.objects.filter(
            Q(name__endswith='.mp3') | Q(name__endswith='.wav'), Q(name__endswith='.ogg') & Q(owner=self.user))
        return initial_files

    def get_video(self):
        initial_files = EncryptedFileTree.objects.filter(Q(name__endswith='.mp4') | Q(
            name__endswith='.avi') | Q(name__endswith='.mkv') | Q(name__endswith='.mov') & Q(owner=self.user))
        return initial_files

    def get_picture(self):
        initial_files = EncryptedFileTree.objects.filter(
            Q(name__endswith='.jpg') | Q(name__endswith='.jpeg') | Q(name__endswith='.png') & Q(owner=self.user))
        return initial_files

    def get_document(self):
        initial_files = EncryptedFileTree.objects.filter(Q(name__endswith=('.pdf')) | Q(
            name__endswith='.docx') | Q(name__endswith='.doc') | Q(name__endswith='.txt') & Q(owner=self.user))
        return initial_files

    # checked

    def get_encrypted(self, fileTree: EncryptedFileTree, from_path: str) -> bool:
        save_to = fileTree.get_complete_path()
        key = fileTree.encryption_key
        return Encrypt.encrypt(from_path, save_to, key)

    # checked
    def get_decrypted(self, fileTree: EncryptedFileTree) -> str:
        # Get the complete path of the encrypted file
        encrypted_path = fileTree.get_complete_path()

        with open(encrypted_path, "rb") as f:
            data = f.read()

        decrypted_data = Encrypt.decrypt(data, fileTree.encryption_key)
        return decrypted_data
    # checked for a file

    def export(self, fileTree, to):
        if fileTree.is_directory:
            new_to = os.path.join(to, fileTree.name).replace("\\", "/")
            try:
                os.mkdir(new_to)
            except FileExistsError:
                pass
            for child in self.get_children(fileTree):
                self.export(child, new_to)
        else:
            decrypted_data = self.get_decrypted(fileTree)
            temp_dir = tempfile.TemporaryDirectory()
            temp_path = os.path.join(temp_dir.name, fileTree.name)
            with open(temp_path, "wb") as f:
                f.write(decrypted_data)
            export_path = os.path.join(to, fileTree.name).replace("\\", "/")
            shutil.move(temp_path, export_path)

    def export_temp(self, fileTree) -> str:
        decrypted_data = self.get_decrypted(fileTree)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = os.path.join(self.temp_dir.name, fileTree.name)
        with open(self.temp_path, "wb") as f:
            f.write(decrypted_data)
        return self.temp_path

    # Checked
    def insert_file(self, file, parentFileTree):
        new_file = EncryptedFileTree.objects.create(name=get_name_from_path(
            file), parent_directory=parentFileTree, owner=self.user, encryption_key=get_encryption_key())
        self.get_encrypted(new_file, file)
        return new_file

    # Checked
    def insert_folder(self, folder, fileTree):
        new_folder = self.create_folder(get_name_from_path(folder), fileTree)
        files = os.listdir(folder)

        for file in files:
            file_path = os.path.join(folder, file).replace("\\", "/")
            if os.path.isfile(file_path):
                self.insert_file(file_path, new_folder)
            elif os.path.isdir(file_path):
                self.insert_folder(file_path, new_folder)
        return new_folder

    # Checked
    def create_folder(self, folder, fileTree):
        new_folder = EncryptedFileTree.objects.create(
            name=folder, parent_directory=fileTree, owner=self.user)
        return new_folder

    # checked
    def is_file(self, id):
        return EncryptedFileTree.objects.get(id=id).is_file

    # checked
    def get_encrypted_file_tree(self, id):
        return EncryptedFileTree.objects.get(id=id)

    # checked
    def delete_fileTree(self, id):
        if not EncryptedFileTree.objects.filter(id=id).exists():
            return False
        fileTree = EncryptedFileTree.objects.get(id=id)
        if fileTree.is_file:
            complete_path = fileTree.get_complete_path()
            fileTree.delete()
            os.remove(complete_path)
        else:
            for file in self.get_children(fileTree):
                self.delete_fileTree(file.id)
            fileTree.delete()
        return True

    def set_storage_location(self, location):
        if location:
            self.user.directory = location
            self.user.has_toured = True
            self.user.save()
            return True
        return False
