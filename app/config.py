import os
import uuid

class Config:
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload'
    SERVER_PATH = ROOT + UPLOAD_PATH

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    # SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = str(uuid.uuid4())
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    USER = os.environ.get('POSTGRES_USER', 'admin')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'admin')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5532)
    DB = os.environ.get('POSTGRES_DB', 'mydb')

