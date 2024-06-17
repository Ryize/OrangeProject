from sqlite3 import IntegrityError

from flask import Blueprint, request, redirect, render_template, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from ..models import User
register = Blueprint('register', __name__)


@register.route('/register', methods=['GET', 'POST'])
def register():
    """
    Обрабатывает страницу регистрации. При GET запросе отображает страницу
    регистрации.
    При POST запросе создает нового пользователя и, если регистрация прошла
    успешно, выполняет вход и перенаправляет на главную страницу.

    Returns:
        werkzeug.wrappers.Response: Объект Response с перенаправлением:
            - на главную страницу при успешной регистрации
            - обратно на страницу регистрации при возникновении ошибки.
     """
    if request.method == 'GET':
        return render_template('register.html')
    login = request.form.get('login')
    password = request.form.get('password')
    if not (3 < len(login) < 32 and 3 < len(password) < 32):
        flash('Логин и пароль должны быть от 4 до 31 символов.')
        return redirect(url_for('register'))
    password = generate_password_hash(password)
    user = User(login=login, password=password)
    try:
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    except IntegrityError:
        flash('Данный логин уже используется.')
        return redirect(url_for('register'))
    # Пользователь с таким логином уже зарегистрирован
