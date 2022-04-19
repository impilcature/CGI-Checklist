"""
This module has select, delete, update of tables with commands in string forms.  
This may not be necessary with SQLalchemy  Look at inner workings to be sure.

"""
import os
from flask_sqlalchemy import SQLAlchemy

from flaskapi import app, basedir

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "cgi-checklist.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init db
db = SQLAlchemy(app)

