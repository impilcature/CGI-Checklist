from flask import Flask
from flask_sqlalchemy import sqlalchemy

db = SQLAlchemy(app)




"""
This module supports the following schema:

CREATE TABLE IF NOT EXISTS Role (     
        RoleID       INT     NOT NULL,
        Role char(50) NOT NULL,
        PRIMARY KEY (RoleID)	
);
"""
class Role(db.Model):
	__tablename__='Role'
	RoleID=db.Column(db.Integer(),primary_key=True)
	Role=db.Column(db.String(25),nullable=False)

"""
 CREATE TABLE IF NOT EXISTS Address (
         AddressID    INT    NOT NULL,  
         Street1  char(25)   NOT NULL,
         Street2    char(25),
         City 		CHAR(13)        NOT NULL,
         State     char(25)   NOT NULL,
         PostalCode char(5) NOT NULL,
         PRIMARY KEY (AddressID)      
  );
"""
class Address(db.Model):
	__tablename__='Address'
	AddressID=db.Column(db.Integer(),primary_key=True)
	Street1=db.Column(db.String(25),nullable=False)
	Street2=db.Column(db.String(25))
	City=db.Column(db.String(25),nullable=False)
	State=db.Column(db.String(25),nullable=False)
	PostalCode=db.Column(db.String(25),nullable=False)
	commands = db.Relationship()

"""
CREATE TABLE IF NOT EXISTS Command (
		CommandID     INT    NOT NULL,
		UIC      Char(25)  NOT NULL,
		Name		CHAR(50)   	      NOT NULL,
		Region		CHAR(50)   	      NOT NULL,
		Address_AddressID INT NOT NULL,
		Foreign key (Address_id) REFERENCES Address(AddressID),
		PRIMARY KEY (CommandID)
  );
  """
class Command(db.Model):
	__tablename__='Command'
	CommandID=db.Column(db.Integer(),primary_key=True)
	UIC=db.Column(db.String(25),nullable=False)
	Name=db.Column(db.String(25),nullable=False)
	Region=db.Column(db.String(25),nullable=False)
	Address_AddressID=db.Column(db.Integer())

"""
  CREATE TABLE IF NOT EXISTS Checklist (
		ChecklistID INT NOT NULL,
		Name CHAR(25) NOT NULL
        Reference CHAR(50) NOT NULL,
		RevisionDate DATE NOT NULL,
		Assessment CHAR(25),
		Footer CHAR(25),
		Applicability CHAR(25),
        primary key (ChecklistID),
);
"""
class Checklist(db.Model):
	__tablename__='Checklist'
	RoleID=db.Column(db.Integer(),primary_key=True)
	Role=db.Column(db.String(25),nullable=False)

"""
CREATE TABLE IF NOT EXISTS Reference (
		ReferenceID INT NOT NULL,
        Title TEXT NOT NULL,
		Page TEXT,
		Paragragh TEXT,
        PRIMARY KEY (ReferenceID)
	);  
"""
class Reference(db.Model):
	__tablename__='Reference'
	RoleID=db.Column(db.Integer(),primary_key=True)
	Role=db.Column(db.String(25),nullable=False)

"""	

CREATE TABLE IF NOT EXISTS Checklist (
		ChecklistID INT NOT NULL,
		Name CHAR(25) NOT NULL
        Reference CHAR(50) NOT NULL,
		RevisionDate DATE NOT NULL,
		Assessment CHAR(25),
		Footer CHAR(25),
		Applicability CHAR(25),
        primary key (ChecklistID),
);
"""
class Checklist(db.Model):
	__tablename__='Checklist'
	RoleID=db.Column(db.Integer(),primary_key=True)
	Role=db.Column(db.String(25),nullable=False)

"""
CREATE TABLE IF NOT EXISTS Subsection (
		SubsectionID INT NOT NULL,
		Title Char(25) NOT NULL,
		PRIMARY KEY (SubsectionID)
  );
"""
class Subsection(db.Model):
	__tablename__='Subsection'
	RoleID=db.Column(db.Integer(),primary_key=True)
	Role=db.Column(db.String(25),nullable=False)

"""
CREATE TABLE IF NOT EXISTS Question (
		QuestionID INT NOT NULL,
        Verbiage TEXT NOT NULL,
		Results TEXT,
		Reference_ReferenceID INT,
		Foreign key (Reference_ReferenceID) REFERENCES Reference(ReferenceID),
        PRIMARY KEY (QuestionID);
	);
"""
class Question(db.Model):
	__tablename__='Question'
	RoleID=db.Column(db.Integer(),primary_key=True)
	Role=db.Column(db.String(25),nullable=False)

"""	
CREATE TABLE IF NOT EXISTS Person (
		PersonID     INT       NOT NULL,
		LastName      CHAR(25)   NOT NULL,
		FirstName CHAR(25) NOT NULL,
		Phone Char(25) NOT NULL,
		Command_CommandID INT NOT NULL,
		Role_RoleID INT NOT NULL,
		Address_AddressID INT NOT NULL,
		PRIMARY KEY (PersonID),
		Foreign key (CommandID) REFERENCES Command(CommandID),
		Foreign key (Role_ID) REFERENCES Role(RoleID),
		Foreign key (Address_id) REFERENCES Address(AddressID)
  );	

"""

class Person(db.Model):
	__tablename__='Person'
	RoleID=db.Column(db.Integer(),primary_key=True)
	Role=db.Column(db.String(25),nullable=False)
