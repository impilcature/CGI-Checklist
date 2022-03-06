from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'SQLITE:///cgiDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


