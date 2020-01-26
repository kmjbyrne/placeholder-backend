from datetime import datetime

from flask_electron.sqlalchemy.declarative import db
from flask_electron.sqlalchemy.declarative import DeclarativeBase


class Task(DeclarativeBase):
    __tablename__ = 'task'
    label = db.Column(db.String(120), nullable=True)
    created = db.Column(db.Date, nullable=True)
    completed = db.Column(db.Date, nullable=True)

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)
    project = db.relationship('ProjectModel', backref='tasks', cascade='all', uselist=False)

    def __repr__(self):
        return self.label


class Tasktype(DeclarativeBase):
    __tablename__ = 'tasktype'
    name = db.Column(db.String(120), nullable=True)
    desc = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return self.name
