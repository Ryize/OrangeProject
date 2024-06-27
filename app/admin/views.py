from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from ..extensions import db

from ..models.posts import Post

admin = Admin(name='Admin Panel', template_mode='bootstrap4')

# Создание представления для модели
class PostsModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True


    # Колонки которые будут отображаться
    column_list = ['id', 'title', 'content', 'author', 'published']

    #Колонки доступные для поиска
    column_searchable_list = ['title']

    # Колонки по которым можно производить сортировку
    column_sortable_list = ['id', 'published']

    # Поля которые будут отображаться в форме создания/отображения
    form_columns = ('title', 'content', 'author', 'published')

    admin.add_view(ModelView(Post, db.session))