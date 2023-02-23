import os
from django.db.models import ImageField


def get_path_to_image(image: ImageField) -> str:
    """This function return a string of absolute path to the image object (django.db.models.ImageField)."""
    current_file_path = os.path.abspath(__file__)
    parent_directory_path = os.path.abspath(
        os.path.join(current_file_path, os.pardir))
    parent_directory_path = parent_directory_path.replace('\\', '/')
    try:
        return parent_directory_path + image.url
    except ValueError as e:
        return None

def get_name_from_path(path):
    return path.split("/")[-1]

def get_encryption_key():
    return "1234"
