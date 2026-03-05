# SQL Database Creation & Data Insertion

This section covers the foundational steps for setting up a SQL database, including table creation (DDL) and initial data population (DML).

## 📋 Overview

Before you can query data, you need to:
1. Define the database structure (create tables)
2. Establish relationships between tables
3. Populate the database with initial data

This folder contains the SQL scripts to accomplish all three steps.

## 📁 Files in This Folder

- `README.md` - This documentation file
- `Schema.png` - Visual diagram of the database structure
- `Create DB.sql` - DDL script to create all tables and constraints
- `Insert Data.sql` - DML script to insert initial data

## 🔧 What is DDL (Data Definition Language)?

DDL commands define the structure of a database:
- **CREATE TABLE** - Defines table structure, columns, and data types
- **PRIMARY KEY** - Uniquely identifies each record
- **FOREIGN KEY** - Creates relationships between tables
- **Constraints** - Rules for valid data (NOT NULL, UNIQUE, CHECK, DEFAULT)

### Example DDL:
```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

## 📊 Database Schema

### Tables in This Database

1. **Employees**
   - Stores employee information
   - Columns: Employee ID, Name, Address, Birthdate, Salary, Department, Supervisor
   - Primary Key: SSN (Social Security Number)
   - Foreign Keys: Department reference, Supervisor reference

2. **Departments**
   - Department information and management
   - Columns: Department ID, Name, Manager ID, Manager Start Date
   - Primary Key: Department ID
   - Foreign Key: Manager SSN references Employees

3. **Projects**
   - Project information and assignments
   - Columns: Project ID, Name, Location, Controlling Department
   - Primary Key: Project ID
   - Foreign Key: Department ID references Departments

4. **Works On** (Assignment Junction Table)
   - Tracks which employees work on which projects
   - Columns: Employee SSN, Project ID, Hours per Week
   - Primary Key: Composite (Employee SSN + Project ID)
   - Foreign Keys: Employee SSN, Project ID

5. **Dependent**
   - Family dependent information for employees
   - Columns: Employee SSN, Dependent Name, Relationship, Gender, Birthdate
   - Primary Key: Composite (Employee SSN + Dependent Name)
   - Foreign Key: Employee SSN

## 🚀 How to Execute

### Step 1: Execute Create DB.sql
```
1. Open your SQL IDE (SQL Server Management Studio, MySQL Workbench, etc.)
2. Connect to your database server
3. Open "Create DB.sql"
4. Review the script to understand the structure
5. Execute the script (Ctrl+A then Execute)
6. Verify tables are created successfully
```

### Step 2: Execute Insert Data.sql
```
1. After successful table creation, open "Insert Data.sql"
2. Review the data being inserted
3. Execute the script
4. Verify data is inserted using SELECT queries
```

### Verification Queries:
```sql
-- Check all tables exist
SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';

-- Count records in each table
SELECT COUNT(*) as EmployeeCount FROM Employees;
SELECT COUNT(*) as DepartmentCount FROM Departments;
SELECT COUNT(*) as ProjectCount FROM Projects;
SELECT COUNT(*) as DependentCount FROM Dependent;
SELECT COUNT(*) as WorksOnCount FROM Works_On;

-- View sample data
SELECT * FROM Employees LIMIT 5;
SELECT * FROM Departments;
```

## 📚 Understanding the Schema from Schema.png

The visual diagram shows:
- **Entity boxes** represent each table
- **Lines connecting boxes** represent relationships (Foreign Keys)
- **Labels on lines** indicate the relationship type (one-to-many, many-to-many)
- **Primary keys** are usually marked with a key symbol

### Key Relationships:
1. **One Department → Many Employees** (One-to-Many)
   - One department can have multiple employees
   - Each employee belongs to one department

2. **One Employee → Many Dependents** (One-to-Many)
   - One employee can have multiple family members
   - Each dependent belongs to one employee

3. **One Project → Many Assignments** (One-to-Many)
   - One project can have multiple employees
   - Via the "Works On" junction table

4. **One Department → Many Projects** (One-to-Many)
   - A department can control multiple projects
   - Each project is controlled by one department

5. **One Department → One Manager** (One-to-One)
   - Each department has a manager (who is an employee)
   - An employee can manage one department

6. **One Employee → Many Supervisees** (One-to-Many)
   - An employee can supervise multiple employees
   - An employee has one supervisor (or NULL for top manager)

## 💡 Key Concepts

### Primary Key (PK)
- Uniquely identifies each record in a table
- Cannot be NULL
- Usually one column, sometimes composite (multiple columns)
- Ensures no duplicate records

### Foreign Key (FK)
- Creates a relationship between two tables
- References a Primary Key in another table
- Maintains **Referential Integrity**
- Prevents orphaned records

### Data Types
Common SQL data types used:
- `INT` - Integer numbers (employee IDs, counts)
- `VARCHAR(n)` - Text up to n characters (names, addresses)
- `DECIMAL(p,s)` - Decimal numbers with p digits, s decimal places (salaries)
- `DATE` - Date values (birthdates, start dates)
- `FLOAT` - Floating-point numbers

### Constraints
Rules that ensure data quality:
- `NOT NULL` - Column must have a value
- `UNIQUE` - Values must be unique in that column
- `PRIMARY KEY` - Uniquely identifies records
- `FOREIGN KEY` - References another table
- `CHECK` - Validates with a condition
- `DEFAULT` - Provides default value if not specified

## 📝 Sample Data Explanation

The Insert Data.sql script populates realistic sample data:
- **Employees**: Various employees in different departments with different salaries
- **Departments**: Several departments with assigned managers
- **Projects**: Projects in different locations controlled by different departments
- **Works On**: Employees assigned to projects with hours worked
- **Dependents**: Family members of employees with relationships

This sample data is used for all queries in the DQL section.

## ⚠️ Important Notes

1. **Referential Integrity**: Foreign keys prevent invalid data
   - Cannot insert an employee for a non-existent department
   - Cannot delete a department that still has employees (usually)

2. **Cascading Rules**: Some databases can automatically update/delete related records
   - ON UPDATE CASCADE - Updates related records automatically
   - ON DELETE CASCADE - Deletes related records automatically

3. **Data Order Matters**: Tables must be created in the correct order
   - Create Departments before Employees (Employees references Departments)
   - Create Employees before Works On and Dependent

4. **NULL Values**: Some columns allow NULL (unknown or not applicable)
   - Example: Supervisor_SSN is NULL for top-level managers

## 🔄 Re-creating the Database

If you need to start fresh:

```sql
-- Drop tables in reverse order (due to foreign keys)
DROP TABLE Works_On;
DROP TABLE Dependent;
DROP TABLE Projects;
DROP TABLE Employees;
DROP TABLE Departments;

-- Then run Create DB.sql again
```

## 🎯 What You'll Learn

After executing these scripts, you'll understand:
- ✅ How to define table structures
- ✅ How to establish relationships between tables
- ✅ Data type selection for different information
- ✅ Constraint usage for data validation
- ✅ How to populate a database with initial data
- ✅ Database normalization principles

## 📖 Next Steps

Once your database is created and populated:
1. Proceed to **02-SQL/02-DQL** to write basic queries
2. Practice simple SELECT statements
3. Learn filtering with WHERE clauses
4. Then move to advanced queries with JOINs and aggregations

## 💡 SQL Execution Tips

1. **Read the script first** - Understand what's being created
2. **Execute in sections** - Run CREATE TABLE statements separately if needed
3. **Check for errors** - Ensure all tables are created successfully
4. **Verify the data** - Run SELECT queries to confirm data is inserted
5. **Keep backup copies** - Save the scripts safely

## 📞 Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| "Table already exists" | Table creation attempted twice | Drop existing table first |
| "Foreign key constraint fails" | Invalid reference | Ensure referenced table exists and PK exists |
| "Duplicate entry for key" | Inserting duplicate PK values | Check data for duplicates |
| "Column not found" | Wrong column name | Verify column names in schema |

## 👤 Author

Karam Yaseen

---

**Last Updated**: March 5, 2026