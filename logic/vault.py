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

    def get_encrypted(self, fileTree: EncryptedFileTree, from_path: str) -> bool:
        # a complete filepath to create. Like: D:/folder/1-file.txt
        save_to = fileTree.get_complete_path()
        return Encrypt.encrypt(from_path, save_to, fileTree.key)

    def get_decrypted(fileTree: EncryptedFileTree) -> str:
        # Get the complete path of the encrypted file
        encrypted_path = fileTree.get_complete_path()

        # Create a temporary directory to save the decrypted file
        temp_dir = tempfile.TemporaryDirectory()
        temp_path = os.path.join(temp_dir.name, fileTree.name)

        with open(encrypted_path, "rb") as f:
            data = f.read()

        decrypted_data = Encrypt.decrypt(data, fileTree.key)
        with open(temp_path, "wb") as f:
            f.write(decrypted_data)

        # Return the path to the decrypted file
        return temp_path

    def export(self, fileTree, to):
        if fileTree.is_directory:
            # if the fileTree is a directory, export all its children recursively
            for child in self.get_children(fileTree):
                self.export(child, os.path.join(to, child.name))
        else:
            # if the fileTree is a file, decrypt it and save to the export path
            temp_path = self.get_decrypted(fileTree)
            export_path = os.path.join(to, fileTree.name)
            shutil.move(temp_path, export_path)

    # Checked
    def insert_file(self, file, fileTree):
        # TODO 1)create a encrypted file tree for the file with parent directory = file tree
        new_file = EncryptedFileTree.objects.create(name=get_name_from_path(
            file), parent_directory=fileTree, owner=self.user, encryption_key=get_encryption_key())
        #     2) encrypt the file from actual path
        self.get_encrypted(new_file, file)
        #     3) returns true, if insertion is successful. else, return false.
        return new_file
    # Checked

    def insert_folder(self, folder, fileTree):
        #   1) call create function and create a folder.   
        #creation of folder
        new_folder = self.create_folder(get_name_from_path(folder), fileTree)
        #   2) loop for all the files one by one using insert_file function.
        files = os.listdir(folder)

        for file in files:
            file_path = os.path.join(folder, file).replace("\\", "/")
            if os.path.isfile(file_path):
                self.insert_file(file_path, new_folder)
                print(file_path)
            elif os.path.isdir(file_path):
                self.insert_folder(file_path, new_folder)
                print(file_path)
        return new_folder

    # Checked
    def create_folder(self, folder, fileTree):
        new_folder = EncryptedFileTree.objects.create(name = folder, parent_directory = fileTree, owner = self.user)
        return new_folder
