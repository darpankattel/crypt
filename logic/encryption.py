class Encrypt:
    @staticmethod
    def decrypt(encryptedFileTree):
        # Create a Fernet object with the key
        f = Fernet(encryptedFileTree.encryption_key)
        # Open the encrypted file and read its contents
        with open(encryptedFileTree.get_complete_path, 'rb') as file:
            encrypted_data = file.read()

        # Decrypt the data
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data
