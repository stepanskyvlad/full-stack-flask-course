import os


class Config:
    SECRET_KY = os.environ.get('SECRET_KEY') or 'secret_string'
