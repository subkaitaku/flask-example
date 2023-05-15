from datetime import datetime

from .database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now()
    )

    def __init__(self, nickname):
        self.nickname = nickname
