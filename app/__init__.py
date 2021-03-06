import logging

from datetime import datetime

from flask import request
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_electron.sqlalchemy.declarative import db
from flask_electron.logger import get_rotating_file_handler

from app._fixtures import tasks
from app.task import task_blueprint
from app.task import tasktype_blueprint
from app.project import project_blueprint

_appstate = Flask(__name__, instance_relative_config=True)

apps = [
    (task_blueprint, '/task'),
    (project_blueprint, '/project'),
    (tasktype_blueprint, '/tasktype'),
]


def verify_release_configuration():
    """
    A pre deployment sanity check to ensure that the minimal required configuration mappings
    are present within the release deploy/config.cfg file.
    Function will look for core config members such as secret key, salts etc...
    :return True / False: True or False if verified or unverified
    :rtype bool
    """
    return False


def error_handler(error):
    if error.code == 404:
        return jsonify(error='This resource/page does not exist.')
    elif error.code == 429:
        return error
    elif error.code == 405:
        return jsonify(error='Method not allowed for this endpoint')
    elif error.code == 500:
        return jsonify(error='An unexpected error has occurred. Support is investigating.')


def create_app(env='DEV'):
    appstate = Flask(__name__, instance_relative_config=True)

    CORS(appstate, resources=r'/api/*')

    config_path = 'app.config.DevelopmentConfig'
    if env == 'DEV':
        config_path = 'app.config.DevelopmentConfig'
    elif env == 'TEST':
        config_path = 'app.config.TestingConfig'
    elif env == 'RELEASE':
        config_path = 'app.config.ReleaseConfig'

    appstate.config.from_object(config_path)
    appstate.config.from_pyfile('config.cfg', silent=True)
    appstate.app_context().push()

    for app, route in apps:
        appstate.register_blueprint(app, url_prefix='/{}{}'.format('api', route))

    appstate.register_error_handler(405, error_handler)
    appstate.register_error_handler(429, error_handler)
    appstate.register_error_handler(404, error_handler)
    appstate.register_error_handler(500, error_handler)

    db.init_app(appstate)
    db.drop_all()
    db.create_all()
    tasks.create()

    @appstate.after_request
    def after_request(response):
        """
        Log all Flask/WSGI output to a separate file for troubleshooting.
        """
        log_format = '%(name)s - %(message)s'
        access_logger = logging.getLogger("app.access")
        access_logger.addHandler(get_rotating_file_handler('/tmp/tzcook.access.log', logging.INFO, log_format))
        access_logger.setLevel(logging.INFO)
        access_logger.info(
            '%s [%s] %s %s %s %s %s %s %s',
            request.remote_addr,
            datetime.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response
    return appstate
