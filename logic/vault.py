from data import EncryptedFileTree
from django.db.models import Q
from functions import get_name_from_path, get_encryption_key
import os

class Vault:
    def __init__(self, user) -> None:
        self.user = user

    def get_initials(self):
        return self.get_children(fileTree=None)

    def get_children(self, fileTree):
        # if it is image then send the content by decrypting too! call get_decrypted()
        initial_files = EncryptedFileTree.objects.filter(
            Q(parent_directory=fileTree) & Q(owner=self.user))
        #TODO send thumbnail for image file
        return initial_files
    
    def get_encrypted(self, fileTree, from_path, to_path):
        return
    
    def get_decrypted(self, fileTree):
        return

    def export(self, fileTree, to):
        if fileTree.is_directory:
            pass
        else:
            pass
    
    #Checked
    def insert_file(self, file, fileTree):
        #TODO 1)create a encrypted file tree for the file with parent directory = file tree
        new_file = EncryptedFileTree.objects.create(name=get_name_from_path(file), parent_directory = fileTree, owner = self.user, encryption_key = get_encryption_key())
        #     2) encrypt the file from actual path
        new_encrypted_file = self.get_encrypted(new_file, file, new_file.get_complete_path())
        #     3) returns true, if insertion is successful. else, return false.
        return new_file
    #Checked
    def insert_folder(self, folder, fileTree):
        #   1) call create function and create a folder.
        
        #creation of folder
        new_folder = self.create_folder( get_name_from_path(folder), fileTree)
        #   2) loop for all the files one by one using insert_file function.
        files = os.listdir(folder)

        for file in files:
            file_path = os.path.join(folder, file).replace("\\","/")
            if os.path.isfile(file_path):
                self.insert_file(file_path, new_folder)
                print(file_path)
        return new_folder

    #Checked
    def create_folder(self, folder, fileTree):
        new_folder = EncryptedFileTree.objects.create(name = folder, parent_directory = fileTree, owner = self.user)
        return new_folder
