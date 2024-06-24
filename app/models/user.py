from ..extensions import db
import json


def load_genres():
    with open('genres.json', 'r') as file:
        return json.load(file)


genres = load_genres()


# Модель для таблицы Пользователь (User)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(60), nullable=False)
    favourite_genres = db.Column(db.String, nullable=True)  # Список жанров в виде строки
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    def set_favourite_genres(self, genre_ids):
        self.favourite_genres = json.dumps(genre_ids)

    def get_favourite_genres(self):
        return json.loads(self.favourite_genres)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()