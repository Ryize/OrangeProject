from flask import Blueprint, render_template, redirect

from ..forms import RegistrationForm
from ..extensions import db, bcrypt
from ..functions import save_picture
from ..models.user import User


user = Blueprint('user', __name__)


@user.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        avatar_filename = save_picture(form.avatar.data)
        new_user = User(username=form.username.data, email=form.email.data,
                    avatar=avatar_filename, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print('Регистрация прошла успешно')
        return redirect('/index.html')
    else:
        print('Ошибка Регистрации')
    return render_template('user/register.html')