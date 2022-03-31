from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

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

# Init ma
ma = Marshmallow(app)

# Classes and models
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), unique=True)

    def __init__(self, role) -> None:
        self.role = role


class RoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "role")


class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uic = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50))
    region = db.Column(db.String(50))
    street1 = db.Column(db.String(100))
    street2 = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    postalcode = db.Column(db.String(10))

    def __init__(
        self, uic, name, region, street1, street2, city, state, postalcode
    ):
        self.uic = uic
        self.name = name
        self.region = region
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.postalcode = postalcode


class CommandSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "uic",
            "name",
            "region",
            "street1",
            "street2",
            "city",
            "state",
            "postalcode",
        )


class Checklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    revisiondate = db.Column(db.String(100))
    assessment = db.Column(db.String(500))
    footer = db.Column(db.String(500))
    applicability = db.Column(db.String(500))

    def __init__(self, name, revisiondate, assessment, footer, applicability):
        self.name = name
        self.revisiondate = revisiondate
        self.assessment = assessment
        self.footer = footer
        self.applicability = applicability


class ChecklistSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "revisiondate", "assessment", "footer", "applicability")


class Reference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    page = db.Column(db.String(10))
    paragraph = db.Column(db.String(500))

    def __init__(self, title, page, paragraph):
        self.title = title
        self.page = page
        self.paragraph = paragraph


class ReferenceSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "page", "paragraph")


class Subsection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    def __init__(self, title):
        self.title = title


class SubsectionSchema(ma.Schema):
    class Meta:
        fields = ("id", "title")


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    street1 = db.Column(db.String(100))
    street2 = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    postalcode = db.Column(db.String(10))

    def __init__(
        self,
        lastname,
        firstname,
        phone,
        addressid,
        street1,
        street2,
        city,
        state,
        postalcode,
    ):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.addressid = addressid
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.postalcode = postalcode


class PersonSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "lastname",
            "firstname",
            "phone",
            "addressid",
            "street1",
            "street2",
            "city",
            "state",
            "postalcode",
        )


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500))
    results = db.Column(db.String(500))

    def __init__(self, question, results, referenceID):
        self.question = question
        self.results = results


class QuestionSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "question",
            "results",
        )


# Init schemas
subsection_schema = SubsectionSchema()
subsection_schema = SubsectionSchema()
question_schema = QuestionSchema()
questions_schema = QuestionSchema()
person_schema = PersonSchema()
persons_schema = PersonSchema()
reference_schema = ReferenceSchema()
references_schema = ReferenceSchema()
checklist_schema = ChecklistSchema()
checklists_schema = ChecklistSchema()
command_schema = CommandSchema()
commands_schema = CommandSchema()
role_schema = RoleSchema()
roles_schema = RoleSchema()


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
    result = checklists_schema.dump(all_checklists)
    return jsonify(result)


# Create a role
@app.route("/role", methods=["POST"])
def add_role():
    role = request.json["role"]

    new_role = Role(role)

    db.session.add(new_role)
    db.session.commit()

    return checklist_schema.jsonify(new_role)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
