"""
Flask-MarcoPolo

run_WebCOUNTER.py

To initiate your Flask-MarcoPolo project

"""
import logging
logging.basicConfig(filename="logs/debug.log", filemode="w", level=logging.DEBUG, format="%(name)s %(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("MAIN")
logger.debug("Starting")

from autologging import logged, traced

from flask import Flask
from flask.ext.marcopolo import MarcoPolo
from flask_mongoengine import MongoEngine

# Import all views to be available in this project
from WebCOUNTER.views import error, index, editors

@traced
@logged(logger)
class MainApplication:
    # The directory containing the project (views, templates, static)
    PROJECT_DIR = "./WebCOUNTER"

    # Project conf environment. Dev=Development, Prod=Production
    PROJECT_CONFIG_ENV = "Dev"

    # The project configuration relative to $project_name.module.class
    PROJECT_CONFIG = "WebCOUNTER.config.%s" % (PROJECT_CONFIG_ENV)

    def __init__(self):
        self.__log.debug("__init__")
        self.__log.debug("calling MarcoPolo.init")
        app = MarcoPolo.init(app=Flask(__name__),
                             config=self.PROJECT_CONFIG,
                             project_dir=self.PROJECT_DIR)
        self.__log.debug("calling MongoEngine")
        db = MongoEngine(app)

        self.__log.debug("setting self.run to app.run")
        self.run = app.run

if __name__ == "__main__":
    logger.debug("initing __main__")
    logger.debug("creating MainApplication")
    app = MainApplication()
    app.run()
