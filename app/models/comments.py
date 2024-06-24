from ..extensions import db
from datetime import datetime

# Модель для таблицы Комментарии (Comments)
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

    def __repr__(self) -> str:
        return f"Comment('{self.username}', '{self.date_posted}', '{self.text[:20]}')"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()