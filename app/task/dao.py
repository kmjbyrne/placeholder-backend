from flask_electron.dao.base import BaseDAO

from .models import Task


class TaskDAO(BaseDAO):
    json = False

    def __init__(self, *args, **kwargs):
        super().__init__(Task, *args, **kwargs)
        self.model = Task
