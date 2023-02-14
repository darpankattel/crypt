from django.contrib.auth import authenticate
from django.utils import timezone
from data import User, AppUser


class CryptAuthException(Exception):
    """Base class for exceptions in CryptAuth."""
    pass


class InvalidCredentialsException(CryptAuthException):
    """Raised when invalid credentials are provided."""
    pass


class InvalidPasswordsException(CryptAuthException):
    """Raised when the password and confirm password don't match."""
    pass


class InvalidUsernameException(CryptAuthException):
    """Raised when the username is empty."""
    pass


class UsernameAlreadyExistsException(CryptAuthException):
    """Raised when the username of the signing up user already esists."""
    pass


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
            return AppUser.objects.get(user=self.user)
        return self.user

    def signup(self, username, first_name, last_name, email, password, confirm_password):
        if not (password == confirm_password):
            raise InvalidPasswordsException(
                "Password and Confirm Password donot match.")
        if not username:
            raise InvalidUsernameException("Username cannot be empty.")
        if not User.objects.filter(username=username).exists():
            new_user = User.objects.create(
                username=username, email=email, password=password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return AppUser.objects.create(user=new_user)
        raise UsernameAlreadyExistsException("Username already exists.")

    def logout(self):
        self.user = None

    def is_authenticated(self):
        return self.user is not None and self.user.is_authenticated

    def get_current_user(self):
        return self.user
