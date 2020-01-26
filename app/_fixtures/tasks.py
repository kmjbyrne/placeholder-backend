from datetime import datetime

from app.project.models import ProjectModel
from app.task.models import Task


SAMPLES = ['test-project']


def create():
    for item in SAMPLES:
        project = ProjectModel()
        project.created = datetime.now()
        project.active = 'Y'
        project.name = item
        project.label = item
        project.save()

        model = Task()
        model.created = datetime.now()
        model.active = 'Y'
        model.label = item
        model.project_id = project.id
        model.save()

