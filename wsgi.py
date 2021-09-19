from core import create_app, db
from sqlalchemy import event
from models import *
import os
import sqlite3
import os

# call create_app() to create and configure flask app
app = create_app('default' or os.getenv('FLASK_CONFIG'))

# spatialite path
spatialite_path = os.getenv('spat_path')
os.environ['PATH'] = spatialite_path + ';' + os.environ['PATH']

# create server instance from app factory
app = create_app(os.getenv("FLASK_CONFIG") or "default")

# add extension to sqlite3
with app.app_context():
    @event.listens_for(db.engine, "connect")
    def load_spatialite(dbapi_conn, connection_record):
        dbapi_conn.enable_load_extension(True)
        dbapi_conn.load_extension('mod_spatialite')
