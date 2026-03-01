-- Dept
INSERT INTO Dept (Dnum, hiredate, DName, Dno, MrgSSN)
VALUES
(1, '2020-01-10', 'IT', NULL, NULL),
(2, '2020-02-15', 'HR', NULL, NULL),
(3, '2020-03-20', 'Finance', NULL, NULL);


-- Employee
INSERT INTO Employee (SSN, BD, Gender, FirstName, LastName, Dno, Superid)
VALUES
('E100', '1980-05-10', 'M', 'Ahmed', 'Ali', 1, NULL),
('E101', '1985-07-15', 'F', 'Sara', 'Mohamed', 2, NULL),
('E102', '1990-09-20', 'M', 'Omar', 'Hassan', 1, 'E100'),
('E103', '1992-11-25', 'F', 'Mona', 'Ibrahim', 3, NULL),
('E104', '1995-01-30', 'M', 'Khaled', 'Youssef', 3, 'E103');


-- Update Dept Managers
UPDATE Dept SET MrgSSN = 'E100' WHERE Dnum = 1;
UPDATE Dept SET MrgSSN = 'E101' WHERE Dnum = 2;
UPDATE Dept SET MrgSSN = 'E103' WHERE Dnum = 3;


-- Locations
INSERT INTO Locations (Dnum, loc)
VALUES
(1, 'Cairo'),
(1, 'Alex'),
(2, 'Giza'),
(3, 'Mansoura');


-- Project
INSERT INTO Project (Pnum, PName, Dnum, loc, City)
VALUES
(10, 'System', 1, 'Building A', 'Cairo'),
(20, 'Website', 1, 'Building B', 'Alex'),
(30, 'Recruitment', 2, 'Building C', 'Giza'),
(40, 'Audit', 3, 'Building D', 'Mansoura');


-- Dependent
INSERT INTO Dependent (SSN, BD, Gender, DName)
VALUES
('E100', '2010-05-01', 'F', 'Nour'),
('E100', '2012-06-02', 'M', 'Youssef'),
('E101', '2015-07-03', 'F', 'Laila');


-- Work
INSERT INTO Work (SSN, Pnumber, hours)
VALUES
('E100', 10, '2024-01-01'),
('E102', 10, '2024-01-02'),
('E102', 20, '2024-01-03'),
('E101', 30, '2024-01-04'),
('E103', 40, '2024-01-05'),
('E104', 40, '2024-01-06');