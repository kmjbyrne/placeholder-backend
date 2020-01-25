
from flask_electron.dao.base import BaseDAO

from .models import ProjectModel


class ProjectDAO(BaseDAO):
    json = False

    def __init__(self, *args, **kwargs):
        super().__init__(ProjectModel, *args, **kwargs)
        self.model = ProjectModel
