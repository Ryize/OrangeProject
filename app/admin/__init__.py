from .views import admin


def init_admin(app):
    admin.init_app(app)
