from flask import Blueprint, render_template
from ..extensions import db

main = Blueprint('main', __name__)

@main.route('/index', methods=['GET'])
@main.route('/', methods=['GET'])
def index():
    """
    Обрабатывает главную страницу приложения, отображая базовый шаблон.

    Returns:
        str: HTML-шаблон 'base.html' для отображения главной страницы.
    """
    return render_template('main/index.html')

