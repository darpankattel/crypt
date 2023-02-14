from django.contrib.auth import authenticate
from django.utils import timezone


class CryptAuth:
    """
    This class contains every method required for authentication with the app.
    """

    def __init__(self):
        self.user = None

    def login(self, username, password):
        self.user = authenticate(username=username, password=password)
        if self.user is not None:
            self.user.last_login = timezone.now()
            self.user.save()
        return self.user

    def logout(self):
        self.user = None

    def is_authenticated(self):
        return self.user is not None and self.user.is_authenticated

    def get_current_user(self):
        return self.user
