from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_

# initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# app factory
def create_app(config_name):
    # create app instance
    app = Flask(__name__)

    # configure app
    app.config.from_object(config_[config_name])

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    return app