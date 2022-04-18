
from flask_marshmallow import Marshmallow

from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from flaskapi import app,db

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

