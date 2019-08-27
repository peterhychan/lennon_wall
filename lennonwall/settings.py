import sys
import os

from lennonwall import app

dev_db = 'sqlite:////' + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABSAE_FILE','data.db'))

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)