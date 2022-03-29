from cgitb import text
import logging
from sqlite3 import Date
from typing import Text
from sqlalchemy import (
    ForeignKey,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
)

from sqlalchemy.orm import mapper

#from ..domain import models
from domain.models import Role, Address, Command, Reference, Checklist, Subsection, Question, Person

logger = logging.getLogger(__name__)

metadata = MetaData()


"""
!!!!!!!!!!!  FIND WHAT THIS DOES !!!!!!!!!!!!!!

Pure domain bookmark:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL
date_edited TEXT NOT NULL
"""

roles = Table( 
    "Roles",
    metadata,
    Column("RoleID", Integer, primary_key=True, autoincrement=True),
    Column("Role", String(255), unique=True, Required=True)

)

addresses = Table(
    "Addresses",
    metadata,
    Column("AddressID", Integer, primary_key=True, autoincrement=True),
    Column("Street1", String(255), Required=True),
    Column("Street2", String(255)),
    Column("City", String(255), Required=True),
    Column("State", String(255), Required=True),
    Column("PostalCode", String(255), Required=True)
)

commands = Table(
    "Commands",
    metadata,
    Column("CommandID", primary_key=True, autoincrement=True),
    Column("UIC", String(255), Required=True),
    Column("Name", String(255), Required=True),
    Column("Region", String(255), Required=True),
    Column("AddressID", ForeignKey(addresses.AddressID), Required=True)# FOREIGNKEY
)

references = Table(
    "References",
    metadata,
    Column("ReferenceID", Integer, autoincrement=True, primary_key=True),
    Column("Title", String(255), Required=True),
    Column("Page", String(255)),
    Column("Paragraph", String(255))
)

checklists = Table(
    "Checklists",
    metadata,
    Column("ChecklistID", Integer, primary_key=True, autoincrement=True),
    Column("Name", String(255), Required=True),
    Column("ReferenceID", String(255), ForeignKey(references.ReferenceID), Required=True ),# FOREIGNKEY
    Column("RevisionDate", Date, Required=True),
    Column("Assessment", String(255), Required=True),
    Column("Footer", Text),
    Column("Applicability", String(255))
)

subsections = Table( # THERE SHOULD BE MORE COLUMNS HERE!!!!!!!!!!!!!!!!!
    "Subsections",
    metadata,
    Column("SubsectionID", Integer, primary_key=True, autoincrement=True),
    Column("Title", String(255), Required=True)
)

questions = Table(
    "Questions",
    metadata,
    Column("QuestionID", Integer, autoincrement=True, primary_key=True),
    Column("Question", Text, Required=True),
    Column("Results", Text,),
    Column("Reference", Integer)
)

persons = Table(
    "Persons",
    metadata,
    Column("PersonID", Integer, primary_key=True, autoincrement=True),
    Column("LastName", String(255), Required=True),
    Column("FirstName", String(255), Required=True),
    Column("Phone", String(255)),
    Column("CommandID", Integer, ForeignKey(commands.CommandID)),
    Column("RoleID", Integer, ForeignKey(roles.RoleID)),
    Column("AddressID", Integer, ForeignKey=(addresses.AddressID))
)   

def start_mappers():
    logger.info("string mappers")
    roles_mapper = mapper(Role, roles)
    addresses_mapper = mapper(Address, addresses)
    commands_mapper = mapper(Command, commands)
    checklists_mapper = mapper(Checklist, checklists)
    subsections_mapper = mapper(Subsection, subsections)
    questions_mapper = mapper(Question, questions)
    reference_mapper = mapper(Reference, references)
    persons_mapper = mapper(Person, persons)