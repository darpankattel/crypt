"""
This file will contain codes to test the logic level of the app.
"""
if __name__ == "__main__":
    """
    WARNING: Donot change the position of the below code
    """
    import sys
    import os
    import django

    sys.path.insert(0, os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'orm')))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
    django.setup()

    # every code reside below this

    # Let this be here
    # This is where the authenticate functions are used
    from logic import CryptAuth, Vault
    from functions import get_path_to_image
    from data import EncryptedFileTree
    username = "darpan.kattel"
    password = "Darpan+423219"
    first_name = "darpan"
    last_name = "kattel"
    confirm_password = "Darpan+423219@"
    email = "darpankattel1@gmail.com"

    auth = CryptAuth()
    # user = auth.signup(username, first_name, last_name,
    #                    email, password, confirm_password)
    # print(user)
    # print(auth.is_authenticated())
    user = auth.login(username, password)
    print(user)
    if user:
        print(auth.is_authenticated())
        print(auth.get_current_user().has_toured)
        print(get_path_to_image(auth.get_current_user().picture))
        myvault = Vault(auth.get_current_user())
        # print(myvault.get_initials())
        # myvault.insert_folder("D:/", None)
        # new_folder = myvault.create_folder(folder = "DarpanBabu", fileTree = EncryptedFileTree.objects.get(id=3))
        # print(new_folder)
        # myvault.insert_file("D:/hello.txt", EncryptedFileTree.objects.get(id=6))
        # myvault.insert_folder("D:/New folder", EncryptedFileTree.objects.get(id=6))
        # file = EncryptedFileTree.objects.create()
        # myvault.insert_file("D:/test/1st-test.txt", None)

        # myvault.get_encrypted(
        #     EncryptedFileTree.objects.get(id=18), "D:/test/1st-test.txt")
        myvault.export(EncryptedFileTree.objects.get(
            id=18), "D:/Crypt/exported/")
        # files = os.listdir("D:/New folder")

        # for file in files:
        #     file_path = os.path.join("D:/New folder", file).replace("\\","/")
        #     print(file_path)
