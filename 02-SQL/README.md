# SQL Training - Database Design & Query Practice

This section contains comprehensive SQL training materials covering database design, database creation, data manipulation, and advanced querying techniques.

## 📚 Sections Overview

### 1. Database Design (ERD & Mapping)
Foundation for understanding the database structure (see `01-Database-Design` folder):
- **Entity-Relationship Diagrams (ERD)**: Visual representation of database entities and relationships
- **Mapping**: Conversion from logical ER model to physical relational schema
- **Normalization**: Organizing data to reduce redundancy and improve integrity
- **Schema Design**: Understanding primary keys, foreign keys, and relationships

### 2. Database Creation & Data Insertion
Practical setup and data initialization:
- **DDL Statements**: Creating tables, defining constraints, establishing relationships
- **DML Statements**: Inserting initial data into the database
- Schema design and normalization principles

### 3. DQL (Data Query Language) - Basic Queries
Fundamental querying techniques:
- **SELECT Statements**: Retrieving and filtering data
- **WHERE Clauses**: Apply conditions to filter results
- **Column Selection**: Choosing specific columns vs. entire records
- **Basic Filtering**: Comparisons, ranges, conditions
- **Data Aliasing**: Creating meaningful column names in results

### 4. Advanced Queries
Complex query patterns and operations:
- **JOINS**: Combining data from multiple tables
- **Aggregation**: GROUP BY, aggregate functions (SUM, AVG, COUNT, MIN, MAX)
- **Subqueries**: Nested queries for complex filtering
- **Set Operations**: UNION combining multiple result sets
- **EXISTS/IN**: Advanced filtering techniques
- **Data Modification**: UPDATE and INSERT operations for existing data
- **Data Deletion**: DELETE operations with proper considerations

## 📁 Folder Structure

```
02-SQL/
├── README.md                          (This file)
├── sql_complete_guide.py              (📚 COMPLETE EXPLANATION GUIDE)
├── 01- Create DB & Insert Data/
│   ├── README.md                      (Database setup guide)
│   ├── Create DB.sql                  (Table creation scripts)
│   ├── Insert Data.sql                (Data insertion scripts)
│   └── Schema.png                     (Visual database schema)
├── 02- DQL/
│   ├── README.md                      (Basic queries documentation)
│   ├── SQLQuery2.sql                  (Basic query solutions)
│   └── SQLQuery3.sql                  (Additional examples)
└── 03- Advanced Queries/
    ├── README.md                      (Advanced queries documentation)
    └── SQLQuery1.sql                  (Advanced query solutions)
```

## 🎯 Learning Path

Follow this sequence for optimal learning:

1. **Start with Database Design** (01-Database-Design folder)
   - Understand the conceptual model
   - Learn how entities relate to each other

2. **Create Database & Insert Data** (02-SQL/01- Create DB & Insert Data/)
   - Execute DDL statements to create tables
   - Execute DML statements to populate data
   - Verify schema structure

3. **Write Basic Queries** (02-SQL/02- DQL/)
   - Master SELECT statements
   - Learn filtering with WHERE
   - Practice simple data retrieval

4. **Attempt Advanced Queries** (02-SQL/03- Advanced Queries/)
   - Combine multiple tables with JOINS
   - Use aggregation functions
   - Create complex nested queries
   - Practice data modification operations

## Key SQL Concepts

### DDL (Data Definition Language)
Commands that define database structure:
- `CREATE TABLE` - Create new tables
- `ALTER TABLE` - Modify table structure
- `DROP TABLE` - Remove tables
- `PRIMARY KEY` - Uniquely identify records
- `FOREIGN KEY` - Establish relationships between tables

### DML (Data Manipulation Language)
Commands that work with data:
- `INSERT` - Add new records
- `UPDATE` - Modify existing records
- `DELETE` - Remove records
- `SELECT` - Retrieve data

### DQL (Data Query Language)
Commands for querying data:
- `SELECT` - Retrieve specific columns/rows
- `FROM` - Specify tables to query
- `WHERE` - Filter records based on conditions
- `JOIN` - Combine data from multiple tables
- `GROUP BY` - Aggregate data by categories
- `ORDER BY` - Sort results
- `HAVING` - Filter grouped results

## Database Schema Overview

The training database typically includes:
- **Employees**: Employee records with salary, department, supervisor info
- **Departments**: Department information and managers
- **Projects**: Project details and controlling departments
- **Works On**: Assignment of employees to projects with hours
- **Dependent**: Family dependent information

## 📖 Topics Covered

### Database Design & Structure
- ✅ Entity-Relationship Diagrams (ERD)
- ✅ Normalization (1NF, 2NF, 3NF)
- ✅ Primary and Foreign Keys
- ✅ Relationships (One-to-One, One-to-Many, Many-to-Many)
- ✅ Constraints and Data Integrity

### DDL (Data Definition Language)
- ✅ CREATE TABLE statements
- ✅ Data types and constraints
- ✅ ALTER TABLE operations
- ✅ DROP TABLE operations

### DML (Data Manipulation Language)
- ✅ INSERT statements
- ✅ UPDATE statements
- ✅ DELETE statements

### Query Types (DQL)
- ✅ Simple SELECT queries
- ✅ Filtering with WHERE conditions
- ✅ Comparisons (=, !=, <, >, BETWEEN, IN)
- ✅ Pattern matching (LIKE with wildcards)
- ✅ Multiple table joins (INNER, LEFT, RIGHT, FULL)
- ✅ Aggregation functions (COUNT, SUM, AVG, MIN, MAX)
- ✅ GROUP BY and HAVING clauses
- ✅ Subqueries and nested queries
- ✅ Set operations (UNION)
- ✅ EXISTS keyword for existence checks
- ✅ CASE statements for conditional logic

### Data Modification
- ✅ INSERT statements
- ✅ UPDATE statements with conditions
- ✅ DELETE statements with cascading considerations
- ✅ Data integrity and constraints

### Advanced Operations
- ✅ Aliases for tables and columns
- ✅ Calculated columns
- ✅ Sorting results
- ✅ Limiting results
- ✅ Handling NULL values
- ✅ Joining multiple tables

## � Where to Start: Guide Files

**Using the complete guide:**
- 📚 Read `sql_complete_guide.py` for detailed explanations of concepts
- 🎓 Reference it while working through each section
- 💡 Use it to understand WHY queries work the way they do

The guide covers:
- Database design fundamentals (ERD, normalization, mapping)
- DDL statements (CREATE, ALTER, DROP)
- DML statements (INSERT, UPDATE, DELETE)
- DQL fundamentals (SELECT, WHERE, JOINs)
- Advanced techniques (GROUP BY, aggregations, subqueries)
- Best practices and common mistakes

## 💡 Tips for Success

1. **Study the design first** - Understand the database structure in 01- Create DB section
2. **Always backup data** before running UPDATE or DELETE
3. **Test filters** in a WHERE clause before applying to actual queries
4. **Use aliases** for complex queries to improve readability
5. **Understand your data** - review schema before querying
6. **Start simple** - master basic SELECT before complex JOINs
7. **Use meaningful column names** in results for clarity
8. **Practice often** - try writing queries without looking at solutions
9. **Read query explanations** in the README files in each folder

## Common Query Patterns

### Get Total Count
```sql
SELECT COUNT(*) FROM employees;
```

### Get Average Salary by Department
```sql
SELECT department_id, AVG(salary) 
FROM employees 
GROUP BY department_id;
```

### Find Employees with Salary > Average
```sql
SELECT * FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### Join Multiple Tables
```sql
SELECT e.first_name, e.last_name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_no = d.dept_no;
```

## 🚀 Next Steps After This Section

- Learn **advanced SQL** features (views, stored procedures, triggers)
- Practice **performance optimization** and query execution plans
- Work with **real-world databases** and datasets
- Explore **database administration** tasks

## 📝 Notes

- All SQL scripts are written in standard SQL syntax
- Some queries may need adaptation for your specific SQL dialect (MySQL, SQL Server, Oracle, PostgreSQL)
- Comments in query files explain the intent and technique
- Solution files show working implementations

## 👤 Author

Karam Yaseen

---

**Last Updated**: March 5, 2026