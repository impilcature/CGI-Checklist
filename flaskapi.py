
"""
lists all the app.route for the API functionality itself
"""
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import repository.models as models

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "cgi-checklist.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init db
db = SQLAlchemy(app)

# Create a Checklist
@app.route("/checklist", methods=["POST"])
def add_checklist():
    name = request.json["name"]
    revisiondate = request.json["revisiondate"]
    assessment = request.json["assessment"]
    footer = request.json["footer"]
    applicability = request.json["applicability"]

    new_checklist = models.Checklist(name, revisiondate, assessment, footer, applicability)

    db.session.add(new_checklist)
    db.session.commit()

    return models.checklist_schema.jsonify(new_checklist)

# Get All checklist
@app.route("/checklist", methods=["GET"])
def get_checklists():
    all_checklists = models.Checklist.query.all()
    result = models.checklist_schema.dump(all_checklists,many=True)
    return models.checklist_schema.jsonify(result, many=True)


# Create a role
@app.route("/role", methods=["POST"])
def add_role():
    role = request.json["role"]

    new_role = models.Role(role)

    db.session.add(new_role)
    db.session.commit()

    return models.role_schema.jsonify(new_role)

# Get All roles
@app.route("/roles", methods=["GET"])
def get_roles():
    all_roles = models.Role.query.all()
    result = models.role_schema.dump(all_roles,many=True)
    return models.role_schema.jsonify(result, many=True)

def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

# Run Server
if __name__ == "__main__":
    init_db()
    app.run(debug=True)