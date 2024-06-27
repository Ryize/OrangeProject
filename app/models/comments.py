from ..extensions import db
from datetime import datetime

# Модель для таблицы Комментарии (Comments)
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Comment('{self.username}', '{self.date_posted}', '{self.text[:20]}')"
