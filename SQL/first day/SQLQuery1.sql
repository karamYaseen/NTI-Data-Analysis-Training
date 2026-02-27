create table Dept (
	Dnum int NOT NULL Primary key ,
	hiredate date null,
	DName varchar(25)  NOT NULL,
	Dno int,
	MrgSSN varchar(20),
	--foreign key (MrgSSN) references Employee(SSN)
)

create table Employee (
	SSN Varchar(20) NOT NULL Primary key ,
	BD date null,
	Gender Varchar(1) check (Gender IN ('F' , 'f' , 'M','m')),
	FirstName varchar(25)  NOT NULL,
	LastName varchar(25)  NOT NULL,
	Dno int,
	Superid varchar(20)
	foreign key (Dno) references Dept(Dnum),
	foreign key (Superid) references Employee
)
alter table Dept
Add foreign key (MrgSSN) references Employee(SSN)

create table Locations (
	Dnum int ,
	loc varchar(25)  NOT NULL,
	Primary key (Dnum,loc),
	foreign key (Dnum) references Dept(Dnum)
)
create table Project (
	Pnum int NOT NULL Primary key ,
	PName varchar(25)  NOT NULL,
	Dnum int ,
	loc varchar(25) ,
	City varchar(25) ,
	foreign key (Dnum) references Dept(Dnum)
)
create table Dependent (
	SSN Varchar(20)  ,
	BD date null,
	Gender Varchar(1) check (Gender IN ('F' , 'f' , 'M','m')),
	DName varchar(25) ,
	Primary key (SSN,DName),
	foreign key (SSN) references Employee(SSN)
)
create table Work (
	SSN Varchar(20)  ,
	Pnumber int,
	hours date  ,
	Primary key (SSN,Pnumber),
	foreign key (Pnumber) references Project(Pnum),
	foreign key (SSN) references Employee(SSN)
)
