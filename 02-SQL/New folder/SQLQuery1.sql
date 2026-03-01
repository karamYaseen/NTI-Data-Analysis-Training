/*
1.	Display (Using Union Function)
	a.	 The name and the gender of the dependence that's gender is Female and depending on Female Employee.
	b.	 And the male dependence that depends on Male Employee.
*/
select d.Dependent_name, d.Sex 
	from Dependent d
	where d.Sex = 'F' and 
	d.ESSN in ( select ssn from Employee 
	where Employee.Sex = 'F')
union
select d.Dependent_name, d.Sex 
	from Dependent d
	where d.Sex = 'M' and 
	d.ESSN in ( select ssn from Employee 
	where Employee.Sex = 'M')

/*
2.	For each project, list the project name and the total hours per week (for all employees) spent on that project.
*/
select p.Pname,sum(w.hours) [total hours per week] from Project p
join Works_for w
on p.Pnumber = w.Pno
group by p.Pname

/*
3.	Display the data of the department which has the smallest employee ID over all employees' ID.
*/
select d.* from Departments d
where d.Dnum in 
(select dno  from Employee where ssn in
(select min(ssn) from Employee ))

--(select dno from Employee where ssn = 102660 

/*
4.	For each department, retrieve the department name and the maximum, minimum and average salary of its employees.
*/
select d.Dname, Max(e.Salary) as Max_Salary, min(e.Salary) as Min_Salary, avg(e.salary) Avg_Salary from Departments d, Employee e
where d.Dnum =e.Dno
group by d.Dname



/*
5.	List the full name of all managers who have no dependents.
*/
select distinct (e.Fname + ' ' + e.Lname) as Manager_Name from Employee e,Departments d, Dependent dt
where e.Dno = d.Dnum and e.SSN = dt.ESSN
and d.MGRSSN is not null

/*
6.	For each department-- if its average salary is less than the average salary of all employees-- display its number, name and number of its employees.
*/
select d.Dname,d.Dnum,count(e.ssn) [number of employees] from Departments d, Employee e
where d.Dnum = e.Dno 
group by d.Dnum,d.Dname
having avg(salary) < (select avg(salary) from Employee)


/*
7.	Retrieve a list of employees names and the projects names they are working on ordered by department number and within each department, ordered alphabetically by last name, first name.
*/
select (e.Fname + ' ' + e.Lname) as Employee_Name,p.Pname from Employee e
join Departments d
on e.Dno = d.Dnum
join Project p
on d.Dnum = p.Dnum
order by d.Dnum,e.Fname,e.Lname

/*
8.	Try to get the max 2 salaries using subquery
*/
select distinct e.salary from Employee e
where e.Salary in ( select distinct top (2) salary from Employee order by Salary desc )


/*
9.	Get the full name of employees that is similar to any dependent name
*/
select distinct (e.Fname + ' ' + e.Lname) as Employee_Name from Employee e 
join Dependent d
on e.SSN = d.ESSN and ((d.Dependent_name like '%' + e.Fname +'%' )or (e.Lname like '%' + d.Dependent_name +'%') )
--select * from Dependent

/*
10.	Display the employee number and name if at least one of them have dependents (use exists keyword) self-study.
*/
select e.SSN, (e.Fname + ' ' + e.Lname) as Employee_Name from Employee e 
where exists (
select 1 from Dependent d where e.SSN = d.ESSN)

/*
11.	In the department table insert new department called "DEPT IT" , with id 100, employee with SSN = 112233 as a manager for this department. The start date for this manager is '1-11-2006'
*/
--select * from Departments
insert into Departments
values('DEPT IT',100,112233,'1-11-2006')	

/*
12.	Do what is required if you know that : Mrs.Noha Mohamed(SSN=968574)  moved to be the manager of the new department (id = 100), and they give you(your SSN =102672) her position (Dept. 20 manager) 
	a.	First try to update her record in the department table
	b.	Update your record to be department 20 manager.
	c.	Update the data of employee number=102660 to be in your teamwork (he will be supervised by you) (your SSN =102672)
*/
update Departments 
set MGRSSN = 968574 
where Dnum = 100

update Departments 
set MGRSSN = 102672
where Dnum = 20

update Employee 
set Superssn = 102672 
where ssn = 102660
/*
13.	Unfortunately the company ended the contract with Mr. Kamel Mohamed (SSN=223344) so try to delete his data from your database in case you know that you will be temporarily in his position.
Hint: (Check if Mr. Kamel has dependents, works as a department manager, supervises any employees or works in any projects and handle these cases).
*/
--SELECT * FROM Employee
--SELECT * FROM Departments
--SELECT * FROM Dependent
--SELECT * FROM Works_for


DELETE FROM Dependent
WHERE ESSN = 223344;

UPDATE Employee
SET Superssn = 102672
WHERE Superssn = 223344;

UPDATE Departments
SET MGRSSN = NULL
WHERE MGRSSN = 223344;

DELETE FROM Works_for
WHERE ESSn = 223344;

DELETE FROM Employee
WHERE SSN = 223344;

/*
14.	Try to update all salaries of employees who work in Project ‘Al Rabwah’ by 30%
*/

UPDATE Employee
SET Salary = 1.3 * Salary
WHERE SSN IN (SELECT ESSN FROM Works_for JOIN Project ON Works_for.Pno = Project.Pnumber AND Project.Pname = 'Al Rabwah')
