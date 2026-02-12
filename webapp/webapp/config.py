import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    DEBUG = os.getenv('DEBUG', 1)
    DJANGO_ALLOWED_HOSTS = os.getenv(
        'DJANGO_ALLOWED_HOSTS', '127.0.0.1'
    ).split(",")
