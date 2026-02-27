-- task 1
select * from Employee

-- task 2
select Fname as First_Name , Lname as Last_Name , Salary, Dno	as depatment_num
from Employee

-- task 3
select pname, plocation ,Dname
from project p, Departments d
where p.Dnum= d.Dnum

-- task 4
select e.fname + ' ' + e.lname as [Empeloyee name ],
		(e.Salary *12*.1) as [ANNUAL SALERY] 
from Employee e

-- task 5
select e.SSN as Emb_ID,e.fname + ' ' + e.lname as [Empeloyee name ]
from Employee e
where e.Salary  > 1000

-- task 6
select e.SSN as Emb_ID,e.fname + ' ' + e.lname as [Empeloyee name ]
from Employee e
where (e.Salary *12)  > 10000

--task 7
select e.fname + ' ' + e.lname as [Empeloyee name ],
		e.Salary
from Employee e
where e.Sex = 'F'

-- task 8
select d.Dnum , d.Dname
from Departments d
where d.MGRSSN = 968574

-- task 9
select p.Pnumber, p.Pname, p.Plocation
from Project p
where p.Dnum = 10