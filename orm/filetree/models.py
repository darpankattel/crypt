from django.db import models
from user.models import AppUser


class EncryptedFileTree(models.Model):
    """
    This Model represents a file or a folder with its name, unique id, owner, encryption key and parent directory.
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    parent_directory = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    encryption_key = models.CharField(max_length=255, null=True, blank=True)

    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def is_file(self):
        return bool(self.encryption_key)

    @property
    def is_directory(self):
        return not self.encryption_key

    def is_owner(self, user):
        return bool(self.owner == user)

    def get_relative_path(self):
        path = self.name
        current_node = self
        while current_node.parent_directory is not None:
            current_node = current_node.parent_directory
            path = f"{current_node.name}/{path}"
        return f"/{path}"

    def get_complete_path(self):
        return f"{self.owner.directory}{self.id}-{self.name}"
