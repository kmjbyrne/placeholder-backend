from flask import Blueprint
from flask_electron.blueprint.core import CoreBlueprint

from .dao import TaskDAO
from .models import Task
from .models import Tasktype

task_blueprint = CoreBlueprint(
    'task',
    __name__,
    dao=TaskDAO,
    model=Task
)

tasktype_blueprint = CoreBlueprint(
    'tasktype',
    __name__,
    model=Tasktype
)
