from cryptography.fernet import Fernet


class Encrypt:
    """
    A class with collected methods for encryption process. Most often used only as a class, not instantiated.
    """
    @staticmethod
    def encrypt(from_path: str, to_path: str, key: str) -> bool:
        """
        A method to encrypt a file from 'from_path' and save the file to 'to_path'.
        """
        with open(from_path, 'rb') as f:
            data = f.read()
        key = bytes(key, 'utf-8')
        # print(key)
        # print(len(key))
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data)
        with open(to_path, 'wb') as f:
            f.write(encrypted_data)
            return True

    @staticmethod
    def decrypt(data: str, key: str) -> str:
        """
        A method to decrypt the data and return the decrypted data.
        """
        key = bytes(key, 'utf-8')
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(data)
        return decrypted_data
