class Vault:
    def __init__(self, user) -> None:
        self.user = user

    def get_initials(self):
        return
    
    def get_children(self, fileTree):
        # if it is image then send the content by decrypting too! call get_decrypted()
        return
    
    def get_decrypted(self, fileTree):
        return

    def export(self, fileTree, to):
        if fileTree.is_directory:
            pass
        else:
            pass
    
    def insert_file(self, file, fileTree):
        return
    
    def insert_folder(self, folder, fileTree):
        return
    
    def create_folder(self, folder, fileTree):
        pass