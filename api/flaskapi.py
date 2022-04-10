"""
lists all the app.route for the API functionality itself
"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ..services.database import db, Role, Checklist, checklist_schema, role_schema
from ..repository.models import subsection_schema, person_schema, question_schema, reference_schema, checklist_schema, command_schema, role_schema
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


# Create a Checklist
@app.route("/checklist", methods=["POST"])
def add_checklist():
    name = request.json["name"]
    revisiondate = request.json["revisiondate"]
    assessment = request.json["assessment"]
    footer = request.json["footer"]
    applicability = request.json["applicability"]

    new_checklist = Checklist(name, revisiondate, assessment, footer, applicability)

    db.session.add(new_checklist)
    db.session.commit()

    return checklist_schema.jsonify(new_checklist)

# Get All checklist
@app.route("/checklist", methods=["GET"])
def get_checklists():
    all_checklists = Checklist.query.all()
    result = checklist_schema.dump(all_checklists,many=True)
    return checklist_schema.jsonify(result, many=True)


# Create a role
@app.route("/role", methods=["POST"])
def add_role():
    role = request.json["role"]

    new_role = Role(role)

    db.session.add(new_role)
    db.session.commit()

    return role_schema.jsonify(new_role)

# Get All roles
@app.route("/role", methods=["GET"])
def get_roles():
    all_roles = Role.query.all()
    result = role_schema.dump(all_roles,many=True)
    return role_schema.jsonify(result, many=True)
