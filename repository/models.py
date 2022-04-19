
from flask_marshmallow import Marshmallow

from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

from flaskapi import app
import services.database as databasepy

# Init ma
ma = Marshmallow(app)

# Classes and models
class Role(databasepy.db.Model):
    id = databasepy.db.Column(databasepy.db.Integer, primary_key=True)
    role = databasepy.db.Column(databasepy.db.String(50), unique=True)

    def __init__(self, role) -> None:
        self.role = role


class RoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "role")


class Command(databasepy.db.Model):
    id = databasepy.db.Column(databasepy.db.Integer, primary_key=True)
    uic = databasepy.db.Column(databasepy.db.String(20), unique=True)
    name = databasepy.db.Column(databasepy.db.String(50))
    region = databasepy.db.Column(databasepy.db.String(50))
    street1 = databasepy.db.Column(databasepy.db.String(100))
    street2 = databasepy.db.Column(databasepy.db.String(100))
    city = databasepy.db.Column(databasepy.db.String(50))
    state = databasepy.db.Column(databasepy.db.String(50))
    postalcode = databasepy.db.Column(databasepy.db.String(10))

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


class Checklist(databasepy.db.Model):
    id = databasepy.db.Column(databasepy.db.Integer, primary_key=True)
    name = databasepy.db.Column(databasepy.db.String(100))
    revisiondate = databasepy.db.Column(databasepy.db.String(100))
    assessment = databasepy.db.Column(databasepy.db.String(500))
    footer = databasepy.db.Column(databasepy.db.String(500))
    applicability = databasepy.db.Column(databasepy.db.String(500))

    def __init__(self, name, revisiondate, assessment, footer, applicability):
        self.name = name
        self.revisiondate = revisiondate
        self.assessment = assessment
        self.footer = footer
        self.applicability = applicability


class ChecklistSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "revisiondate", "assessment", "footer", "applicability")


class Reference(databasepy.db.Model):
    id = databasepy.db.Column(databasepy.db.Integer, primary_key=True)
    title = databasepy.db.Column(databasepy.db.String(50))
    page = databasepy.db.Column(databasepy.db.String(10))
    paragraph = databasepy.db.Column(databasepy.db.String(500))

    def __init__(self, title, page, paragraph):
        self.title = title
        self.page = page
        self.paragraph = paragraph


class ReferenceSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "page", "paragraph")


class Subsection(databasepy.db.Model):
    id = databasepy.db.Column(databasepy.db.Integer, primary_key=True)
    title = databasepy.db.Column(databasepy.db.String(50))

    def __init__(self, title):
        self.title = title


class SubsectionSchema(ma.Schema):
    class Meta:
        fields = ("id", "title")


class Person(databasepy.db.Model):
    id = databasepy.db.Column(databasepy.db.Integer, primary_key=True)
    lastname = databasepy.db.Column(databasepy.db.String(50))
    firstname = databasepy.db.Column(databasepy.db.String(50))
    phone = databasepy.db.Column(databasepy.db.String(50))
    street1 = databasepy.db.Column(databasepy.db.String(100))
    street2 = databasepy.db.Column(databasepy.db.String(100))
    city = databasepy.db.Column(databasepy.db.String(50))
    state = databasepy.db.Column(databasepy.db.String(50))
    postalcode = databasepy.db.Column(databasepy.db.String(10))

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


class Question(databasepy.db.Model):
    id = databasepy.db.Column(databasepy.db.Integer, primary_key=True)
    question = databasepy.db.Column(databasepy.db.String(500))
    results = databasepy.db.Column(databasepy.db.String(500))

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
question_schema = QuestionSchema()
person_schema = PersonSchema()
reference_schema = ReferenceSchema()
checklist_schema = ChecklistSchema()
command_schema = CommandSchema()
role_schema = RoleSchema()