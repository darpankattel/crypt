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

    from ui import HomeUI

    app = HomeUI()
    app.mainloop()
