from flask import Flask
from .extensions import db
from .config import Config
# from .routes.tools import tool
# from .routes.main import main
from .admin import init_admin
from .routes.main import main
from .routes.register import registration


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(registration)
    app.register_blueprint(main)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    init_admin(app)

    return app
