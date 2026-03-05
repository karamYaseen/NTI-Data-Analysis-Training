# SQL Complete Guide - Database Design & Queries
# A comprehensive explanation of SQL fundamentals and advanced techniques

"""
╔══════════════════════════════════════════════════════════════╗
║                      SQL COMPLETE GUIDE                      ║
║               Database Design & Query Techniques             ║
╚══════════════════════════════════════════════════════════════╝

This guide explains all SQL concepts covered in the training.
Each section includes explanations, examples, and best practices.
"""

# ==========================================
# SECTION 1: DATABASE DESIGN FUNDAMENTALS
# ==========================================

"""
DATABASE DESIGN - CREATING EFFECTIVE DATA STRUCTURES

Before writing SQL queries, you must understand how databases are designed.
Good design ensures data integrity, efficiency, and scalability.
"""

# ===== ENTITY-RELATIONSHIP DIAGRAM (ERD) =====
"""
An ERD is a visual representation of how entities (tables) relate to each other.

Key Concepts:
- ENTITY: A real-world object (Employee, Department, Project)
- ATTRIBUTE: Properties of an entity (Name, Salary, Start_Date)
- RELATIONSHIP: How entities relate to each other

Relationship Types:
- ONE-TO-ONE (1:1): One employee has one manager's office
- ONE-TO-MANY (1:N): One department has many employees
- MANY-TO-MANY (M:N): Many employees work on many projects

Example ERD (Company Database):
┌─────────────────┐         ┌──────────────────┐
│   DEPARTMENT    │         │    EMPLOYEE      │
├─────────────────┤      ┌─ ├──────────────────┤
│ dept_id (PK)    │──┐   │  │ emp_id (PK)      │
│ dept_name       │  │ 1:N │  │ emp_name         │
│ budget          │  │   └─ │  │ salary           │
└─────────────────┘  │      │  │ dept_id (FK)     │
                     │      │  │ manager_id (FK)  │
                     │      └─ └──────────────────┘
                     │
                     └── Relationships:
                         - 1 Department → Many Employees
                         - 1 Employee → 1 Department
"""

# ===== NORMALIZATION =====
"""
Normalization is the process of organizing data to reduce redundancy
and improve data integrity.

Normal Forms (Levels of Normalization):

1NF (First Normal Form):
   - Eliminate repeating groups
   - Each column contains only atomic (indivisible) values
   
   Bad: Student table with multiple phone numbers in one column
   Good: Separate Students and PhoneNumbers tables

2NF (Second Normal Form):
   - Must be in 1NF
   - Remove partial dependencies
   - All non-key columns must depend on the entire primary key
   
   Bad: StudentCourse table with college_id when you already have student_id
   Good: Separate into proper relationships

3NF (Third Normal Form):
   - Must be in 2NF
   - Remove transitive dependencies
   - Non-key columns must not depend on other non-key columns
   
   Bad: Employee table with DepartmentManager (depends on DeptID, not EmpID)
   Good: Reference Department table for manager info
"""

# ===== DATABASE MAPPING =====
"""
Mapping is the process of converting a logical ER model into a physical schema.
It translates the design into actual SQL table structures.

Mapping Rules:

1. ENTITY → TABLE
   Each entity becomes a table
   
   Entity: EMPLOYEE
   ↓
   Table: employees (
       emp_id INT PRIMARY KEY,
       first_name VARCHAR(50),
       last_name VARCHAR(50),
       salary DECIMAL(10, 2)
   )

2. ATTRIBUTE → COLUMN
   Each attribute becomes a column
   Each column has a data type
   
   Data Types:
   - INT, BIGINT: Integers
   - DECIMAL(p,s): Numbers with decimals
   - VARCHAR(n): Variable text up to n characters
   - CHAR(n): Fixed text of n characters
   - DATE: YYYY-MM-DD format
   - DATETIME: Date and time

3. PRIMARY KEY (PK)
   Uniquely identifies each row in a table
   Cannot be NULL
   Usually marked on ERD with underline
   
   Example:
   CREATE TABLE employees (
       emp_id INT PRIMARY KEY,  -- This uniquely identifies each employee
       name VARCHAR(100)
   )

4. FOREIGN KEY (FK)
   Links one table to another
   Establishes relationships
   Should reference the primary key of another table
   
   Example:
   CREATE TABLE employees (
       emp_id INT PRIMARY KEY,
       name VARCHAR(100),
       dept_id INT,
       FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
   )
   -- emp_id is PK in employees
   -- dept_id is FK pointing to departments table

5. ONE-TO-MANY MAPPING
   Add FK to the "many" side
   
   1 Department : Many Employees
   ↓
   departments table: dept_id (PK)
   employees table: dept_id (FK) + other columns

6. MANY-TO-MANY MAPPING
   Create a junction table
   
   Many Employees : Many Projects
   ↓
   Create employee_project table with:
   - emp_id (FK to employees)
   - project_id (FK to projects)
   - hours_worked
   
7. CONSTRAINTS
   Rules that ensure data integrity
   
   PRIMARY KEY: Unique, not null
   FOREIGN KEY: Must exist in parent table
   UNIQUE: Prevent duplicate values
   NOT NULL: Column must have value
   DEFAULT: Default value if none provided
   CHECK: Validate values meet condition
   
   Example:
   CREATE TABLE employees (
       emp_id INT PRIMARY KEY,
       email VARCHAR(100) UNIQUE,
       salary DECIMAL(10,2) CHECK (salary > 0),
       hire_date DATE NOT NULL,
       status VARCHAR(20) DEFAULT 'Active'
   )
"""

# ==========================================
# SECTION 2: SQL BASICS - DDL & DML
# ==========================================

"""
SQL FUNDAMENTALS - Creating and Populating Databases

SQL has several categories:
- DDL: Data Definition Language (structure)
- DML: Data Manipulation Language (data)
- DQL: Data Query Language (retrieval)
"""

# ===== DDL: DATA DEFINITION LANGUAGE =====
"""
DDL statements define the database structure (CREATE, ALTER, DROP)
"""

# Example: CREATE TABLE
"""
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    hire_date DATE NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(dept_id)
);

Breaking it down:
- CREATE TABLE: Creates new table
- emp_id INT PRIMARY KEY: Integer column that uniquely identifies each row
- first_name VARCHAR(50): Text column, max 50 characters
- NOT NULL: This column must have a value
- email VARCHAR(100) UNIQUE: No two employees can have same email
- salary DECIMAL(10,2): Number with 10 total digits, 2 after decimal
- CHECK (salary > 0): Ensures salary is positive
- FOREIGN KEY: Establishes relationship with departments table
"""

# Example: ALTER TABLE
"""
ALTER TABLE employees ADD COLUMN phone VARCHAR(20);
-- Adds new column to existing table

ALTER TABLE employees DROP COLUMN phone;
-- Removes a column

ALTER TABLE employees MODIFY salary DECIMAL(12, 2);
-- Changes column definition
"""

# Example: DROP TABLE
"""
DROP TABLE employees;
-- Deletes entire table and its data
-- Use with caution!
"""

# ===== DML: DATA MANIPULATION LANGUAGE =====
"""
DML statements work with the data (INSERT, UPDATE, DELETE)
"""

# Example: INSERT
"""
INSERT INTO employees (first_name, last_name, salary, department_id)
VALUES ('John', 'Smith', 50000, 1);

-- Insert multiple rows:
INSERT INTO employees (first_name, last_name, salary, department_id) VALUES
('Alice', 'Johnson', 60000, 1),
('Bob', 'Brown', 55000, 2),
('Carol', 'Davis', 65000, 2);

Breaking it down:
- INSERT INTO: Which table to insert data into
- (column names): Which columns you're providing values for
- VALUES: The actual data to insert
"""

# Example: UPDATE
"""
UPDATE employees 
SET salary = 55000 
WHERE emp_id = 5;

-- Update multiple columns:
UPDATE employees 
SET salary = 60000, department_id = 2 
WHERE emp_id = 3;

Breaking it down:
- UPDATE: Which table to update
- SET: Which columns to change and new values
- WHERE: Condition for which rows to update
- IMPORTANT: Always include WHERE clause (except when updating all rows intentionally!)
"""

# Example: DELETE
"""
DELETE FROM employees 
WHERE emp_id = 5;

-- Delete multiple rows:
DELETE FROM employees 
WHERE salary < 30000;

Breaking it down:
- DELETE FROM: Which table to delete from
- WHERE: Condition for which rows to delete
- WARNING: Always verify WHERE clause before executing!
"""

# ==========================================
# SECTION 3: DQL - QUERYING DATA
# ==========================================

"""
DQL FUNDAMENTALS - Retrieving and Analyzing Data

DQL is used to retrieve, filter, and analyze data.
Most of your SQL work will be DQL queries.
"""

# ===== SELECT STATEMENTS =====
"""
SELECT is the foundation of all data retrieval.

Syntax:
SELECT column_name(s)
FROM table_name
WHERE conditions
ORDER BY column_name;
"""

# Example 1: Simple SELECT
"""
SELECT * FROM employees;
-- Retrieves ALL columns and ALL rows from employees table

SELECT emp_id, first_name, last_name, salary 
FROM employees;
-- Retrieves only specified columns, all rows
"""

# Example 2: Filtering with WHERE
"""
SELECT * FROM employees 
WHERE salary > 50000;
-- Only employees earning more than $50,000

SELECT * FROM employees 
WHERE department_id = 2 AND salary > 55000;
-- Multiple conditions using AND

SELECT * FROM employees 
WHERE department_id = 2 OR department_id = 3;
-- Multiple conditions using OR
"""

# ===== COMPARISON OPERATORS =====
"""
Operators used in WHERE clauses:

=           Equal to
!=, <>      Not equal to
>           Greater than
<           Less than
>=          Greater than or equal to
<=          Less than or equal to
BETWEEN     Range (inclusive)
IN          Match any value in a list
LIKE        Pattern matching
IS NULL     Check for NULL values
IS NOT NULL Check for non-NULL values

Examples:
SELECT * FROM employees WHERE salary = 50000;
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000;
SELECT * FROM employees WHERE department_id IN (1, 2, 3);
SELECT * FROM employees WHERE first_name LIKE 'J%';  -- Starts with J
SELECT * FROM employees WHERE email IS NOT NULL;
"""

# ===== SORTING RESULTS =====
"""
ORDER BY sorts the results

SELECT * FROM employees 
ORDER BY salary DESC;  -- Highest salary first

SELECT * FROM employees 
ORDER BY department_id ASC, salary DESC;
-- First by department (ascending)
-- Then by salary within each department (descending)

Common options:
ASC  - Ascending (default)
DESC - Descending
"""

# ===== LIMITING RESULTS =====
"""
LIMIT restricts number of rows returned

SELECT * FROM employees 
ORDER BY salary DESC 
LIMIT 5;  -- Top 5 highest paid employees

SELECT * FROM employees 
LIMIT 10 OFFSET 5;  -- Skip first 5, show next 10
"""

# ===== DISTINCT =====
"""
DISTINCT removes duplicate values

SELECT DISTINCT department_id 
FROM employees;
-- Shows each unique department only once

SELECT COUNT(DISTINCT department_id) 
FROM employees;
-- Counts how many different departments exist
"""

# ===== ALIASES =====
"""
Aliases create temporary names for columns or tables

SELECT first_name AS 'First Name', 
       last_name AS 'Last Name', 
       salary AS 'Annual Salary'
FROM employees;

SELECT e.emp_id, e.first_name, d.dept_name
FROM employees e
JOIN departments d ON e.department_id = d.dept_id;
-- e = alias for employees, d = alias for departments
"""

# ==========================================
# SECTION 4: ADVANCED QUERIES
# ==========================================

"""
ADVANCED SQL - Complex Data Retrieval and Analysis
"""

# ===== JOINS =====
"""
JOINs combine data from multiple tables.

Types of Joins:

1. INNER JOIN
   Returns only rows where condition matches both tables
   
   SELECT e.first_name, e.last_name, d.dept_name
   FROM employees e
   INNER JOIN departments d ON e.department_id = d.dept_id;
   -- Shows employees and their departments
   -- Only those employees who have a department

2. LEFT JOIN (LEFT OUTER JOIN)
   Returns all rows from LEFT table + matching rows from RIGHT table
   
   SELECT e.first_name, d.dept_name
   FROM employees e
   LEFT JOIN departments d ON e.department_id = d.dept_id;
   -- Shows all employees, even those without departments
   -- department.name will be NULL if no match

3. RIGHT JOIN (RIGHT OUTER JOIN)
   Returns matching rows from LEFT + all rows from RIGHT table
   
   SELECT e.first_name, d.dept_name
   FROM employees e
   RIGHT JOIN departments d ON e.department_id = d.dept_id;
   -- Shows all departments, even those with no employees

4. FULL OUTER JOIN
   Returns all rows from both tables
   
   SELECT e.first_name, d.dept_name
   FROM employees e
   FULL OUTER JOIN departments d ON e.department_id = d.dept_id;
   -- Shows all employees and all departments
"""

# ===== AGGREGATE FUNCTIONS =====
"""
Aggregate functions calculate values across multiple rows.

Common Functions:

COUNT()   - Count rows
SUM()     - Sum values
AVG()     - Average value
MIN()     - Minimum value
MAX()     - Maximum value

Examples:

SELECT COUNT(*) FROM employees;
-- Total number of employees

SELECT COUNT(DISTINCT department_id) FROM employees;
-- How many different departments

SELECT AVG(salary) FROM employees;
-- Average salary across all employees

SELECT MAX(salary), MIN(salary) FROM employees;
-- Highest and lowest salaries

SELECT SUM(salary) FROM employees;
-- Total salary expenses
"""

# ===== GROUP BY =====
"""
GROUP BY groups rows by one or more columns
Used with aggregate functions

SELECT department_id, COUNT(*) as employee_count
FROM employees
GROUP BY department_id;
-- Count employees in each department

SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id;
-- Average salary by department

SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;
-- Only departments with average salary > $50,000
-- HAVING filters after grouping (vs WHERE filters before grouping)
"""

# ===== SUBQUERIES =====
"""
Subqueries are queries within queries

Example: Find employees earning more than average

SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

Example: Find department with most employees

SELECT dept_name FROM departments
WHERE dept_id = (
    SELECT department_id FROM employees
    GROUP BY department_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

Example: Subquery in FROM clause

SELECT dept_summary.*
FROM (
    SELECT department_id, COUNT(*) as emp_count, AVG(salary) as avg_sal
    FROM employees
    GROUP BY department_id
) AS dept_summary
WHERE dept_summary.emp_count > 5;
"""

# ===== UNION =====
"""
UNION combines results from multiple queries

SELECT first_name, last_name FROM employees
UNION
SELECT manager_name, 'Manager' FROM managers;
-- Combines employee names with manager names

Note: Columns must have same data types and same count
"""

# ===== EXISTS =====
"""
EXISTS checks if subquery returns any rows

SELECT dept_name FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e
    WHERE e.department_id = d.dept_id
);
-- Shows only departments that have employees
"""

# ===== CASE STATEMENTS =====
"""
CASE adds conditional logic to queries

SELECT first_name, salary,
    CASE
        WHEN salary < 40000 THEN 'Entry Level'
        WHEN salary < 60000 THEN 'Mid Level'
        WHEN salary < 80000 THEN 'Senior'
        ELSE 'Management'
    END AS salary_level
FROM employees;

CASE categorizes each employee by salary range
"""

# ==========================================
# SECTION 5: BEST PRACTICES
# ==========================================

"""
WRITING GOOD SQL QUERIES

1. READABILITY
   - Use consistent formatting and indentation
   - Use meaningful aliases
   - Add comments for complex logic
   - Use clear column names in results

2. PERFORMANCE
   - Use WHERE to filter early (reduce rows)
   - SELECT specific columns, not *
   - Use appropriate data types
   - Index frequently searched columns
   - Avoid subqueries when JOIN is possible

3. ACCURACY
   - Always verify your WHERE clause
   - Test on sample data first
   - Use transactions for bulk changes
   - Keep backups before modifications

4. SECURITY
   - Use parameterized queries to prevent SQL injection
   - Don't expose sensitive data unnecessarily
   - Restrict user permissions appropriately
   - Validate all input data

5. COMMON MISTAKES
   - Forgetting WHERE clause in UPDATE/DELETE
   - Using wrong data types
   - Creating unnecessary duplicate rows
   - Not backing up before modifications
   - Missing relationships/foreign keys
"""

# ===== QUERY WRITING TEMPLATE =====
"""
Good SQL Query Structure:

SELECT 
    e.emp_id,
    e.first_name,
    e.last_name,
    e.salary,
    d.dept_name
FROM 
    employees e
INNER JOIN 
    departments d ON e.department_id = d.dept_id
WHERE 
    e.salary > 50000
    AND e.hire_date >= '2020-01-01'
ORDER BY 
    e.salary DESC
LIMIT 10;

Key points:
- Clear table aliases
- Explicit joins
- Specific column selection
- Clear WHERE conditions
- Meaningful sorting
- Result limitation
"""

# ===== DEBUGGING QUERIES =====
"""
When a query doesn't work:

1. Syntax errors:
   - Check spelling
   - Verify table/column names exist
   - Balance parentheses and quotes

2. Logic errors:
   - Test WHERE conditions separately
   - Verify JOIN conditions are correct
   - Check data types match
   - Run step-by-step to find issue

3. Performance issues:
   - Use EXPLAIN to see execution plan
   - Check for missing indexes
   - Limit rows during testing
   - Check for N+1 query problems
"""

# ==========================================
# SUMMARY & QUICK REFERENCE
# ==========================================

"""
KEY TAKEAWAYS:

1. DATABASE DESIGN:
   - ERD shows entity relationships
   - Normalization eliminates redundancy
   - Mapping converts design to tables
   - Primary and foreign keys maintain integrity

2. DDL (Structure):
   - CREATE TABLE: Define table structure
   - ALTER TABLE: Modify structure
   - DROP TABLE: Delete table

3. DML (Data):
   - INSERT: Add new data
   - UPDATE: Modify existing data
   - DELETE: Remove data

4. DQL (Queries):
   - SELECT: Retrieve data
   - WHERE: Filter rows
   - JOIN: Combine tables
   - GROUP BY: Aggregate data
   - ORDER BY: Sort results

5. BEST PRACTICES:
   - Write readable SQL
   - Test before executing
   - Use appropriate data types
   - Optimize performance
   - Always backup before changes
"""

# ===== COMMON QUERY PATTERNS =====
"""
USEFUL PATTERNS:

1. Top N Records:
SELECT TOP 10 * FROM employees ORDER BY salary DESC;

2. Running Count:
SELECT COUNT(*) FROM employees;

3. Find Duplicates:
SELECT column_name, COUNT(*) 
FROM table_name 
GROUP BY column_name 
HAVING COUNT(*) > 1;

4. Date Calculations:
SELECT DATEDIFF(DAY, hire_date, GETDATE()) as days_employed
FROM employees;

5. String Matching:
SELECT * FROM employees 
WHERE first_name LIKE '%John%';

6. NULL Handling:
SELECT * FROM employees 
WHERE commission IS NULL;

7. Multiple Conditions:
SELECT * FROM employees 
WHERE (department_id = 1 OR department_id = 2) 
AND salary > 50000;

8. Data Aggregation by Multiple Groups:
SELECT department_id, YEAR(hire_date), COUNT(*)
FROM employees
GROUP BY department_id, YEAR(hire_date);
"""