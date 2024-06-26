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

    username = "javed.ansari"
    password = "Gotohell@123"
    first_name = "Darpan"
    last_name = "Kattel"
    confirm_password = "Darpan+423219"
    email = "darpankattel1@gmail.com"

    auth = CryptAuth()
    # user = auth.signup(username, first_name, last_name,
    #                    email, password, confirm_password)
    # print(user)
    # print(auth.is_authenticated())
    auth.login(username, password)
    print(auth.is_authenticated())
    print(auth.get_current_user().has_toured)
    print(get_path_to_image(auth.get_current_user().picture))

    myVault = Vault(auth.get_current_user())
    my_files = myVault.get_initials()
    print(my_files)
