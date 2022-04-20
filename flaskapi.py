import os

from flask import Flask, request, jsonify, render_template, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# establish basedir
basedir = os.path.abspath(os.path.dirname(__file__))

# upload configs
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'doc', 'rtf'}

# Init app
app = Flask(__name__)

# set app config for upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


import repository.models as models
import services.database as databasepy

db, app = databasepy.databaseconfig(app, basedir)

db, app, subsection_schema, question_schema, person_schema, reference_schema, checklist_schema, command_schema, role_schema = models.setupdb(db, app)

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

# upload to temp
@app.route('/upload')
def fileuploadtemp():
   return render_template('upload.html')

# upload file	
@app.route('/uploader', methods = ['GET', 'POST'])
def fileupload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

# Run Server
if __name__ == "__main__":
    app.run(debug=True)