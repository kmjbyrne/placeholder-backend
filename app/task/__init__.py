from flask import Blueprint
from flask_electron.blueprint.core import CoreBlueprint

from .dao import TaskDAO
from .models import Task

task_blueprint = CoreBlueprint(
    'category',
    __name__,
    TaskDAO,
    Task
)

# from . import models