from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

manager = LoginManager()
# допилить логин менеджер и миксины (https://github.com/Ryize/Presentations/blob/main/RoadMap%20Flask-Login.md)

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
