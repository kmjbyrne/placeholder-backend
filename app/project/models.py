
from datetime import datetime

from flask_electron.sqlalchemy.declarative import db
from flask_electron.sqlalchemy.declarative import DeclarativeBase


class ProjectModel(DeclarativeBase):
    __tablename__ = 'project'
    name = db.Column(db.String(120), nullable=True)
    created = db.Column(db.Date, nullable=True)
