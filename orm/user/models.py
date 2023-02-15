from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    """
    This Model relates to Django's default User Model (OneToOne) and contains additional information of the user, like, their default storing directory, picture, etc..
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    directory = models.CharField(max_length=1000, null=True, blank=False)
    picture = models.ImageField(
        upload_to="users/", blank=True, null=True)
    has_toured = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    # @property
    # def no_of_dirs(self):
    #     return len(EncryptedFileTree.objects.filter(owner=self.user))

    def __str__(self):
        return f"{self.user.username}"
