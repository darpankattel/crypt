import os
from django.db.models import ImageField


def get_path_to_image(image: ImageField) -> str:
    """This function return a string of absolute path to the image object (django.db.models.ImageField)."""
    current_file_path = os.path.abspath(__file__)
    parent_directory_path = os.path.abspath(
        os.path.join(current_file_path, os.pardir))
    parent_directory_path = parent_directory_path.replace('\\', '/')
    return parent_directory_path + image.url
