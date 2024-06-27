from ..extensions import db
import json
from datetime import datetime

# def load_genres():
#     with open('genres.json', 'r') as file:
#         return json.load(file)

# genres = load_genres()

# Модель для таблицы Посты (Posts)
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    associated_genres = db.Column(db.String, nullable=True)
    comment_count = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, nullable=False)
    def set_associated_genres(self, genre_ids):
        self.associated_genres = json.dumps(genre_ids)

    def get_associated_genres(self):
        return json.loads(self.associated_genres)

    def __repr__(self) -> str:
        return f"Post('{self.title}', '{self.date_posted}')"
