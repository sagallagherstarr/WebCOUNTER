"""
Flask-MarcoPolo

run_WebCOUNTER.py

To initiate your Flask-MarcoPolo project

"""
import logging
logging.basicConfig(filename="logs/debug.log", filemode="w", level=logging.DEBUG, format="%(name) %(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("MAIN")
logger.debug("Starting")

from flask import Flask
from flask.ext.marcopolo import MarcoPolo
from flask_mongoengine import MongoEngine

# Import all views to be available in this project
from WebCOUNTER.views import error, index

# The directory containing the project (views, templates, static)
project_dir = "./WebCOUNTER"

# Project conf environment. Dev=Development, Prod=Production
project_config_env = "Dev"

# The project configuration relative to $project_name.module.class
project_config = "WebCOUNTER.config.%s" % (project_config_env)

# MarcoPolo.init returns the flask app instance
app = MarcoPolo.init(app=Flask(__name__),
                            config=project_config,
                            project_dir=project_dir)
db = MongoEngine(app)

if __name__ == "__main__":
    app.run()
