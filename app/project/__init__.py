
from flask import Blueprint
from flask_electron.blueprint.core import CoreBlueprint

from .dao import ProjectDAO
from .models import ProjectModel

project_blueprint = CoreBlueprint(
    'project',
    __name__,
    ProjectDAO,
    ProjectModel
)

# from . import models
