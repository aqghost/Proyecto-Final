import os
from django.utils.text import slugify

def get_filename(filename):
    return filename.lower()