import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent.parent / '.env.local')


class Config:
    # Django
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    DEBUG = os.getenv('DEBUG', 1)
    DJANGO_ALLOWED_HOSTS = os.getenv(
        'DJANGO_ALLOWED_HOSTS', '127.0.0.1'
    ).split(",")
    DJANGO_LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'WARNING')

    #  Postgres
    POSTGRES_DB = os.getenv('POSTGRES_DB', '')
    POSTGRES_USER = os.getenv('POSTGRES_USER', '')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'db')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
