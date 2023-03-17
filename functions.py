import os
from django.db.models import ImageField
from cryptography.fernet import Fernet
from datetime import datetime


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
    new_arr = path.split("/")[::-1]
    if new_arr[0] == "" or new_arr[0] == None:
        return new_arr[1]
    return new_arr[0]


def get_encryption_key() -> str:
    return Fernet.generate_key().decode('utf-8')


def clearinside(element):
    for el in element.winfo_children():
        el.destroy()


def get_file_extension(fileName: str):
    return fileName.split(".")[::-1][0]


def get_formatted_date(date):
    """
    Takes a datetime object and returns a formatted date string in the format:
    12th Jan, 2022 at 12:00 PM
    """
    # Convert datetime object to string in the format "2022-01-12 12:00:00"
    date_string = date.strftime("%Y-%m-%d %I:%M:%S %p")

    # Convert string to datetime object
    date_time = datetime.strptime(date_string, "%Y-%m-%d %I:%M:%S %p")

    # Get day suffix (e.g. "st" for 1st, "nd" for 2nd, etc.)
    day = date_time.day
    if day in [1, 21, 31]:
        day_suffix = "st"
    elif day in [2, 22]:
        day_suffix = "nd"
    elif day in [3, 23]:
        day_suffix = "rd"
    else:
        day_suffix = "th"

    # Format date string in the format "12th Jan, 2022 at 12:00 PM"
    formatted_date = date_time.strftime(f"%d{day_suffix} %b, %Y at %I:%M %p")

    return formatted_date
