import os
import uuid

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECRET_KEY = str(uuid.uuid4())
    SQLALCHEMY_TRACK_MODIFICATIONS = True