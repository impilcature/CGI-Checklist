-- CGI-CHECKLIST
-- Daniel Green


-- WTAMU Spring 2022
-- CIDM 6330-70 Project

-- Remove Old Schema
DROP SCHEMA IF EXISTS CGI-Checklist;

-- Create New Schema
CREATE SCHEMA IF NOT EXISTS CGI-Checklist;

USE CGI-Checklist;

-- Create tables

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


--  **************** Data Entry Below This Line ****************

-- Turn off safe update mode
SET SQL_SAFE_UPDATES = 0;

-- Do not check foreign key constraints
SET FOREIGN_KEY_CHECKS = 0;

-- Clear Customer Table
DELETE from Customer;

-- Insert Customer Data
INSERT INTO Customer
  (CustomerID,FirstName,LastName,StreetAddress,PostalCode,PhoneNumber,email)
VALUES
  (2,'Giavani','Bulled','518 Arrowood Pass','12345','379-481-6791','gbulled1@army.mil'),
  (3,'Jervis','Coultous','49 Ludington Park','23456','919-596-5875','jcoultous2@dropbox.com'),
  (5,'Emelia','Spurway','3 Utah Terrace','34567','391-919-5684','espurway4@tripod.com'),
  (4,'Alvin','Ivanichev','36821 Boyd Crossing','46778','510-873-3869','aivanichev3@cnn.com'),
  (1,'Alison','Creagh','81 2nd Trail','4567','586-756-9711','acreagh0@facebook.com'),
  (6,'Arlyne','Zannuto','734 Mesta Junction','23456','301-809-9077','azannuto5@buzzfeed.com'),
  (7,'Allin','Doige','9061 Elgar Crossing','2345','491-699-8398','adoige6@huffingtonpost.com'),
  (8,'Debbi','Meconi','321 Heffernan Alley','12456','238-797-7793','dmeconi7@360.cn'),
  (9,'Jules','Teasell','77674 Anzinger Lane','12345','644-966-7391','jteasell8@go.com'),
  (10,'Umberto','Edeson','125 Grover Point','12346','990-628-5698','uedeson9@mail.ru');
  
  -- After Data Entry change CustomerID to auto Increment
  ALTER TABLE Customer MODIFY COLUMN CustomerID INT auto_increment;

-- Clear Item Table
DELETE from Item;

-- Insert Data
INSERT INTO Item
  (ItemID,ItemDescription,AvailableQuantity,UnitSalesPrice,CostPrice)
VALUES
  (1,'Wood 1',35,245.65,233),
  (2,'Vinyl 1',73,70.66,65.39),
  (3,'Stone 1',77,255.71,233.06),
  (4,'Aluminum 1',99,158.62,117.73),
  (5,'Plexiglass A',70,495.76,467.39),
  (6,'Plastic  P1',66,409.45,386.14),
  (7,'Aluminum 2',53,603.5,567.14),
  (8,'Plexiglass  B',8,381.19,349.7),
  (9,'Wood 2',65,639.64,587.28),
  (10,'Steel s1',48,295.73,279.74),
  (11,'Plexiglass  C',82,420.31,386.01),
  (12,'Glass G1',69,396.71,367.34),
  (13,'Steel s2',32,502.33,467.93),
  (14,'Wood 3',2,26.73,25.46),
  (15,'Steel s3',19,483.05,458.14),
  (16,'Granite t1',98,276.98,261.89),
  (17,'Wood 4',54,412.84,376.99),
  (18,'Rubber r1',29,408.75,377.86),
  (19,'Plastic P2',100,474.17,446.83),
  (20,'Glass G2',61,459.65,425.38);

  -- After Data Entry change ItemID to auto Increment
  ALTER TABLE Item MODIFY COLUMN ItemID INT auto_increment;
  
-- Clear Supplier Table
DELETE from Supplier;

-- Insert Data
INSERT INTO Supplier
  (SupplierID,BusinessName,Address,PhoneNumber)
VALUES
  (1,'Senger Inc','702 Hovde Center','279-750-7429'),
  (2,'Gleichner LLC','25 Daystar Circle','474-846-9283'),
  (3,'Stehr, Ebert and Braun','0588 Spaight Crossing','245-140-0943'),
  (4,'Kshlerin, Bednar and Denesik','57 Lawn Pass','359-442-5927'),
  (5,'Hartmann, Ritchie and Buckridge','0 Oak Lane','341-991-9231'),
  (6,'Kautzer LLC','55 Packers Drive','147-555-8000'),
  (7,'Auer, Okuneva and Streich','1333 Nova Drive','576-343-8318'),
  (8,'Abernathy-Purdy','3 Bobwhite Avenue','113-873-3330'),
  (9,'Rogahn, Fisher and Tillman','25305 Clarendon Terrace','793-526-8512'),
  (10,'Hane Inc','11783 Oriole Trail','835-181-9469');
  
    -- After Data Entry change SupplierID to auto Increment
  ALTER TABLE Supplier MODIFY COLUMN SupplierID INT auto_increment;

-- Clear SuppliedItem Table
DELETE from SuppliedItem;

-- Insert Data
INSERT INTO SuppliedItem
  (SuppliedItemID,Item_ItemID,Supplier_SupplierID,RecentPrice,RecentSuppliedQuantity,RecentPurchasedDate)
VALUES
  (1,1,1,233,200,'2021-06-15'),
  (2,1,2,235,150,'2020-12-10'),
  (3,2,8,65.39,200,'2020-10-19'),
  (4,3,9,233.06,100,'2020-12-27'),
  (5,4,8,117.73,100,'2021-02-22'),
  (6,5,5,467.39,200,'2021-02-11'),
  (7,6,7,386.14,50,'2020-10-03'),
  (8,7,9,567.14,20,'2021-02-16'),
  (9,8,5,349.7,20,'2020-12-20'),
  (10,9,1,587.28,100,'2021-06-15'),
  (11,10,4,279.74,70,'2021-11-01'),
  (12,10,6,285,30,'2020-05-01'),
  (13,11,5,386.01,20,'2020-12-04'),
  (14,12,3,367.34,60,'2020-10-22'),
  (15,13,4,467.93,120,'2020-10-11'),
  (16,14,1,25.46,50,'2021-01-16'),
  (17,15,10,458.14,20,'2020-12-08'),
  (18,16,2,261.89,30,'2020-09-27'),
  (19,17,2,376.99,90,'2020-12-05'),
  (20,18,10,377.86,50,'2021-01-12'),
  (21,19,6,446.83,70,'2021-02-13'),
  (22,20,3,425.38,115,'2020-12-11');
  
    -- After Data Entry change SuppliedItemID to auto Increment
  ALTER TABLE SuppliedItem MODIFY COLUMN SuppliedItemID INT auto_increment;

-- Clear Employee Table
DELETE from Employee;

-- Insert Data
INSERT INTO Employee
  (EmployeeID,FirstName,LastName,Role)
VALUES
  (3,'Dorry','Bremen','sales'),
  (4,'Andie','MacCarroll','manager'),
  (6,'Abel','Deschlein','sales'),
  (7,'Georas','Breche','manager'),
  (9,'Lou','Rowlin','sales');
  
    -- After Data Entry change EmployeeID to auto Increment
  ALTER TABLE Employee MODIFY COLUMN EmployeeID INT auto_increment;

-- Clear Invoice Table
DELETE from Invoice;

-- Insert Data
INSERT INTO Invoice
  (InvoiceID,InvoiceDate,InvoiceTime,InvoiceTotal,AmountDue,RunningPaymentTotal,Employee_EmployeeID,InvoicePenalty,Customer_CustomerID)
VALUES
  (101,'2015-01-14','10:55:00',2227.62,2227.62,2000,6,1,2),
  (102,'2015-01-06','11:00:00',2892.19,420.31,200,4,1,3),
  (103,'2015-01-09','16:25:00',3933.25,2892.19,2400,4,1,3),
  (104,'2015-01-14','14:31:00',420.31,3933.25,2350,3,1,2),
  (105,'2015-01-02','9:45:00',5820.93,5820.93,5000,6,1,4),
  (106,'2015-01-15','11:45:00',3844.67,3844.67,3500,7,1,3),
  (107,'2015-01-06','11:00:00',7417.06,4480.25,0,9,1,2),
  (108,'2015-01-05','12:33:00',4480.25,5133.42,0,7,1,5),
  (109,'2015-02-07','10:45:00',5133.42,7417.06,0,7,1,4);
  
    -- After Data Entry change InvoiceID to auto Increment
  ALTER TABLE Invoice MODIFY COLUMN InvoiceID INT auto_increment;
  
-- Make the RunningBalance column store calculate the running balance
ALTER TABLE Invoice
Drop Column RunningBalance,
ADD COLUMN  RunningBalance FLOAT 
GENERATED ALWAYS AS (AmountDue-RunningPaymentTotal) STORED;

-- Clear Payment Table
DELETE from Payment;

INSERT INTO Payment
  (PaymentID,PaymentDate,PaymentAmount,PaymentMethod,Invoice_InvoiceID,Employee_EmployeeID)
VALUES
  (1,'2015-01-14',2000,'CC#  4041595198458061',101,6),
  (2,'2015-01-06',2400,'Cash',102,4),
  (3,'2015-01-09',1150,'cash',103,9),
  (4,'2015-01-15',1200,'Check-WF#34567652',103,4),
  (5,'2015-01-14',100,'CC# 4041595198458060',104,3),
  (6,'2015-01-15',100,'CC#  4041595198458061',104,3),
  (7,'2015-01-02',5000,'CC#4017958222625370',105,6),
  (8,'2015-01-15',3500,'Cash',106,7),
  (9,'2015-01-07',7000,'CC#  4041595198458061',107,9),
  (10,'2015-01-20',417.06,'CC#  4041595198458061',107,7),
  (11,'2015-02-07',5133.42,'CC#4017958222625370',109,7);
  
    -- After Data Entry change PaymentID to auto Increment
  ALTER TABLE Payment MODIFY COLUMN PaymentID INT auto_increment;

-- Clear InvoiceItem Table
DELETE from InvoiceItem;

INSERT INTO InvoiceItem
  (InvoiceItemID,QuantityPurchased,Item_ItemID,Invoice_InvoiceID)
VALUES
  (1,2,19,101),
  (2,2,9,101),
  (3,1,6,102),
  (4,1,8,102),
  (5,5,11,102),
  (6,4,18,103),
  (7,5,20,103),
  (8,1,11,104),
  (9,5,12,105),
  (10,5,1,105),
  (11,3,8,105),
  (12,3,2,105),
  (13,4,10,105),
  (14,1,2,105),
  (15,1,3,106),
  (16,4,8,106),
  (17,5,17,106),
  (18,4,20,107),
  (19,4,12,107),
  (20,5,9,107),
  (21,2,12,107),
  (22,4,17,108),
  (23,5,13,108),
  (24,2,4,108),
  (25,4,10,109),
  (26,1,4,109),
  (27,1,7,109),
  (28,3,3,109),
  (29,5,16,109),
  (30,1,9,109),
  (31,1,12,109);
  
    -- After Data Entry change InvoiceItemID to auto Increment
  ALTER TABLE InvoiceItem MODIFY COLUMN InvoiceItemID INT auto_increment;


-- Safe update mode
SET SQL_SAFE_UPDATES = 1;

-- Check foreign key constraints
SET FOREIGN_KEY_CHECKS = 1;