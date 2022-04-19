
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

import repository.models as models
import services.database as databasepy

# Create a Checklist
@app.route("/checklist", methods=["POST"])
def add_checklist():
    name = request.json["name"]
    revisiondate = request.json["revisiondate"]
    assessment = request.json["assessment"]
    footer = request.json["footer"]
    applicability = request.json["applicability"]

    new_checklist = models.Checklist(name, revisiondate, assessment, footer, applicability)

    databasepy.db.session.add(new_checklist)
    databasepy.db.session.commit()

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

    databasepy.db.session.add(new_role)
    databasepy.db.session.commit()

    return models.role_schema.jsonify(new_role)

# Get All roles
@app.route("/roles", methods=["GET"])
def get_roles():
    all_roles = models.Role.query.all()
    result = models.role_schema.dump(all_roles,many=True)
    return models.role_schema.jsonify(result, many=True)

# Run Server
if __name__ == "__main__":
    app.run(debug=True)