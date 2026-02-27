-- task 1 (Display the Department id, name and id and the name of its manager.)
select d.Dnum as [Department id], d.Dname as [Department name ], 
d.MGRSSN as [manager id], e.fname + ' ' + lname as [Manager name ]

from Departments d
inner join Employee e
on  d.MGRSSN = e.SSN

-- task 2 (Display the name of the departments and the name of the projects under its control.)
select d.Dnum as [Department id], d.Dname as [Department name ], 
 p.Pname as [Project name ]
from Departments d
inner join Project p
on  d.Dnum = p.Dnum

-- task 3 (Display the full data about all the dependence associated with the name of the employee they depend on him/her.)
select d.Dependent_name , d.Sex, d.Bdate,
 e.fname + ' ' + lname as [Employee name ]
from Dependent d
inner join Employee e
on  d.ESSN = e.SSN

-- task 4 (Display the Id, name and location of the projects in Cairo or Alex city)
select  p.Pnumber, p.Pname, p.Plocation
from Project p
where p.City = 'Cairo' or p.City = 'Alex'

-- task 5 (Display the Projects full data of the projects with a name starts with "a" letter.)
select  * from Project p
where p.Pname like 'a%'

-- task 6 (display all the employees in department 30 whose salary from 1000 to 2000 LE monthly)
select  * from Employee e
where e.Dno = 30 and e.Salary between 1000 and 2000

-- task 7
select *
from Employee e , Works_for w , Project p
where   e.SSN = w.ESSn and w.Pno = p.Pnumber and
		e.Dno = 10 and w.Hours >= 10 and p.Pname = 'Al Rawdah'

-- task 8
select * from Employee e ,Employee S
where s.Superssn = e.SSN and (s.fname + ' ' + s.lname) = 'Kamel Mohamed'

-- task 9 
select  e.fname + ' ' + lname as [Employee name ], p.Pname
from Employee e , Project p , Works_for w
where  e.SSN = w.ESSn and w.Pno = p.Pnumber 
order by p.Pname

-- task 10
select p.Pname, d.Dname, e.Lname, e.Bdate ,e.Address
from Employee e , Departments d , Project p
where   e.SSN = d.MGRSSN and d.Dnum = p.Dnum and
		 p.City = 'Cairo'

 -- task 11
select * from Employee e ,Employee S
where s.Superssn = e.SSN 

-- task 12
select d.* ,
 e.*
from Dependent d
right join Employee e
on  d.ESSN = e.SSN

-- task 13
insert into Employee (dno,SSN ,Superssn,salary)
 values ( 30, 102672, 112233, 3000)

 -- task 14
insert into Employee (dno,SSN)
 values ( 30, 102660)

-- task 15
update Employee
set Salary = Salary * 1.2
where