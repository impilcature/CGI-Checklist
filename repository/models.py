from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Completed this model based off of Barky.  The classes from this module should be imported to ORM as string mappers


class Role:
    """
      CREATE TABLE IF NOT EXISTS Role (     
            id       INT     NOT NULL,
            role char(50) NOT NULL,
            PRIMARY KEY (RoleID)	
    );
    """

    def __init__(self, id, role) -> None:
        self.id = id
        self.role = role


class Address:
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

    def __init__(self, id, street1, street2, city, state, postalcode, commands) -> None:
        self.id = id
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.postalcode = postalcode


class Command:
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

    def __init__(self, id, uic, name, region, addressid) -> None:
        self.id = id
        self.uic = uic
        self.name = name
        self.region = region
        self.AddressID = addressid


class Checklist:
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
    
    """

    def __init__(
        self, id, name, referenceid, revisiondate, assessment, footer, applicability
    ) -> None:
        self.id = id
        self.name = name
        self.revisiondate = revisiondate
        self.assessment = assessment
        self.footer = footer
        self.applicability = applicability
        self.referenceid = referenceid


class Reference:
    """
        CREATE TABLE IF NOT EXISTS Reference (
                ReferenceID INT NOT NULL,
                Title TEXT NOT NULL,
                Page TEXT,
                Paragragh TEXT,
                PRIMARY KEY (ReferenceID)
            );  
    """

    def __init__(self, id, title, page, paragraph) -> None:
        self.id = id
        self.title = title
        self.page = page
        self.paragraph = paragraph


class Subsection:
    """	
        CREATE TABLE IF NOT EXISTS Subsection (
                SubsectionID INT NOT NULL,
                Title Char(25) NOT NULL,
                PRIMARY KEY (SubsectionID)
        );
    """

    def __init__(self, id, title) -> None:
        self.id = id
        self.title = title


class Person:
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

    def __init__(
        self, id, lastname, firstname, phone, commandid, roleid, addressid
    ) -> None:
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.commandid = commandid
        self.roleid = roleid
        self.addressid = addressid


class Question:
    """		QuestionID INT NOT NULL,
        Verbiage TEXT NOT NULL,
		Results TEXT,
		Reference_ReferenceID INT,
		Foreign key (Reference_ReferenceID) REFERENCES Reference(ReferenceID),
        PRIMARY KEY (QuestionID);
        """

    def __init__(self, id, question, results, referenceID) -> None:
        self.id - id
        self.question = question
        self.results = results
        self.referenceID = referenceID
