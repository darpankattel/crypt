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

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'orm')))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
    django.setup()

    # every code reside below this


    # Let this be here
    # This is where the authenticate functions are used
    from logic import CryptAuth


    username = "darpan.kattel"
    password = "Darpan+423219@"

    auth = CryptAuth()
    user = auth.login(username, password)
    print(user)
    print(auth.is_authenticated())
