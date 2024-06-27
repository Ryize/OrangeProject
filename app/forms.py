from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    def __init__(self, formdata=_Auto, **kwargs):
        super().__init__(formdata, kwargs)
        self.name = None

    username = StringField('Логин', validators=[DataRequired(), Length(min=3, max=32)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Подтвердите пароль', validators=[DataRequired(),
                                                       EqualTo('password')])
    avatar = FileField('Загрузите аватар', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Зарегистрироваться')