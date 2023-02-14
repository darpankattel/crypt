class DecryptedFile:
    def __init__(self, name, is_directory, owner, encryption_key=None):
        self.name = name
        self.is_directory = is_directory
        self.children = []
        self.owner = owner
        self.encryption_key = encryption_key

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def delete(self):
        # Code to delete the file/directory from the database goes here
        pass

    def rename(self, new_name):
        # Code to rename the file/directory in the database goes here
        self.name = new_name

    def is_file(self):
        return not self.is_directory

    def is_dir(self):
        return self.is_directory

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        # Code to update the owner in the database goes here
        self.owner = new_owner

    def get_encryption_key(self):
        return self.encryption_key

    def set_encryption_key(self, new_key):
        # Code to update the encryption key in the database goes here
        self.encryption_key = new_key
