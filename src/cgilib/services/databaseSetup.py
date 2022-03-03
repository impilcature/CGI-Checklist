from datetime import datetime
from multiprocessing import connection
import sqlite3, os
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey, Column, String, DateTime, Integer, create_engine
from datetime import datetime

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

connection_string="sqlite:///"+os.path.join(BASE_DIR, 'CGI.db')

engine=create_engine(connection_string,echo=True)


