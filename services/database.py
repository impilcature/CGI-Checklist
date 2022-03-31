"""
This module has select, delete, update of tables with commands in string forms.  
This may not be necessary with SQLalchemy  Look at inner workings to be sure.

"""

"""
This module supports the following schema:

CREATE TABLE IF NOT EXISTS Role (     
        RoleID       INT     NOT NULL,
        Role char(50) NOT NULL,
        PRIMARY KEY (RoleID)	
);

 CREATE TABLE IF NOT EXISTS Address (
         AddressID    INT    NOT NULL,  
         Street1  char(25)   NOT NULL,
         Street2    char(25),
         City 		CHAR(13)        NOT NULL,
         State     char(25)   NOT NULL,
         PostalCode char(5) NOT NULL,
         PRIMARY KEY (AddressID)      
  );

CREATE TABLE IF NOT EXISTS Command (
		CommandID     INT    NOT NULL,
		UIC      Char(25)  NOT NULL,
		Name		CHAR(50)   	      NOT NULL,
		Region		CHAR(50)   	      NOT NULL,
		Address_AddressID INT NOT NULL,
		Foreign key (Address_id) REFERENCES Address(AddressID),
		PRIMARY KEY (CommandID)
  );
  
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

CREATE TABLE IF NOT EXISTS Reference (
		ReferenceID INT NOT NULL,
        Title TEXT NOT NULL,
		Page TEXT,
		Paragragh TEXT,
        PRIMARY KEY (ReferenceID)
	);  
	

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

CREATE TABLE IF NOT EXISTS Subsection ( -- Left off here
		SubsectionID INT NOT NULL,
		Title Char(25) NOT NULL,
		PRIMARY KEY (SubsectionID)
  );

CREATE TABLE IF NOT EXISTS Payment (
		PaymentID INT NOT NULL,
		Invoice_InvoiceID INT NOT NULL,
        Employee_EmployeeID INT NOT NULL,
		PaymentDate date NOT NULL,
        PaymentMethod char(25) NOT NULL,
        PaymentAmount FLOAT NOT NULL,
		PRIMARY KEY (PaymentID),
		FOREIGN KEY (Invoice_InvoiceID) REFERENCES Invoice(InvoiceID),
        FOREIGN KEY (Employee_EmployeeID) REFERENCES Employee(EmployeeID)
	);

CREATE TABLE IF NOT EXISTS Question (
		QuestionID INT NOT NULL,
        Verbiage TEXT NOT NULL,
		Results TEXT,
		Reference_ReferenceID INT,
		Foreign key (Reference_ReferenceID) REFERENCES Reference(ReferenceID),
        PRIMARY KEY (QuestionID);
	);
	
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

import sqlite3


class DatabaseManager:
    def __init__(self, database_filename) -> None:
        # added this to persist the name of the database file
        self.database_filename = database_filename
        self.connection = sqlite3.connect(database_filename)

    def __del__(self):
        self.connection.close()