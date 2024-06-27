from sqlite3 import IntegrityError
from flask_login import login_user

from flask import Blueprint, request, redirect, render_template, flash, url_for, \
    Response
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from ..models.user import User
import json



registration = Blueprint('registration', __name__)


@registration.route('/register', methods=['GET', 'POST'])
def register() -> Response | str:
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
        with open('app/models/genres.json', 'r', encoding='utf-8') as f:
            genres = json.load(f)
        return render_template('register.html', genres=genres)

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    favourite_genres = request.form.getlist('favourite_genres')

    if not (3 < len(username) < 32 and 3 < len(password) < 32):
        flash('Логин и пароль должны быть от 4 до 31 символов.')
        return redirect(url_for('registration.register'))

    if password != password2:
        flash('Пароли не совпадают.')
        return redirect(url_for('registration.register'))

    favourite_genres_json = json.dumps(favourite_genres)

    password = generate_password_hash(password)
    user = User(username=username, email=email, password=password,
                favourite_genres=favourite_genres_json)
    try:
        db.session.add(user)
        db.session.commit()
        print(user)
        login_user(user)
        return redirect(url_for('index'))
    except IntegrityError:
        flash('Такой логин или E-mail уже используется!')
        return redirect(url_for('registration.register'))
    # Пользователь с таким логином уже зарегистрирован
