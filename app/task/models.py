from datetime import datetime

from flask_electron.sqlalchemy.declarative import db
from flask_electron.sqlalchemy.declarative import DeclarativeBase


class Task(DeclarativeBase):
    __tablename__ = 'task'
    label = db.Column(db.String(120), nullable=True)
    created = db.Column(db.Date, nullable=True)
    completed = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return self.name
