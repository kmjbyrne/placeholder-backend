#!/usr/bin/env python3
import os
import sys
import textwrap

from sys import exit


def do():
    print('Test')
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    for item in sys.argv[1:]:
        blueprint = item
        arguments = sys.argv

        classname = ''.join([str(i).capitalize() for i in item.replace('_', ' ').split(' ')])

        if blueprint == '':
            print('[x] Cannot create Blueprint. Please provide argument')

        directory = 'app/{}'.format(blueprint)
        if not os.path.exists(directory):
            os.makedirs(directory)

        f = open('app/{}/__init__.py'.format(blueprint), 'w+')
        content = f"""
            from flask import Blueprint
            from flask_electron.blueprint.core import CoreBlueprint
        
            from .dao import {classname}DAO
            from .models import {classname}Model
        
            {blueprint}_blueprint = CoreBlueprint(
                '{blueprint}',
                __name__,
                {classname}DAO,
                {classname}Model
            )
        
            # from . import models
        """
        f.write(textwrap.dedent(content))
        f.close()

        f = open('app/{}/dao.py'.format(blueprint), 'w+')
        content = f"""
            from flask_electron.dao.base import BaseDAO
            
            from .models import {classname}Model
        
        
            class {classname}DAO(BaseDAO):
                json = False
            
                def __init__(self, *args, **kwargs):
                    super().__init__({classname}Model, *args, **kwargs)
                    self.model = {classname}Model
        """

        f.write(textwrap.dedent(content))
        f.close()

        f = open('app/{}/models.py'.format(blueprint), 'w+')
        content = f"""
            from datetime import datetime
        
            from flask_electron.sqlalchemy.declarative import db
            from flask_electron.sqlalchemy.declarative import DeclarativeBase
        
        
            class {classname}Model(DeclarativeBase):
                __tablename__ = '{blueprint}'
                field = db.Column(db.String(120), nullable=True)
        """
        f.write(textwrap.dedent(content))
        f.close()


if __name__ == '__main__':
    do()
