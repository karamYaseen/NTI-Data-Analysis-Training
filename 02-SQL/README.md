# SQL Training - Database Design & Query Practice

This section contains comprehensive SQL training materials covering database design, database creation, data manipulation, and advanced querying techniques.

## � Quick Start (5 minutes)

**New to this SQL training?** Do this first:
1. If you haven't done Database Design (01-Database-Design), start there first
2. Run `Create DB.sql` to set up your database
3. Run `Insert Data.sql` to populate sample data
4. Try simple queries from `02- DQL/SQLQuery2.sql`

**Total Time to Complete Everything**: 6-8 hours

## 📋 Prerequisites & Requirements

### Knowledge Required:
- ✓ Basic database design concepts (from 01-Database-Design)
- ✓ Understand tables, primary keys, foreign keys
- ✓ Comfortable with basic logical operators (AND, OR, NOT)

### Software Required:
- SQL Server Management Studio, MySQL Workbench, or similar
- A SQL database server installed and running
- Text editor for viewing SQL files

### Optional:
- VS Code (for syntax highlighting and file management)
- Git (for version control)

## ⚙️ Environment Setup

### Windows (SQL Server Express):
```powershell
# If using SQL Server Express, ensure it's running
# Access via SQL Server Management Studio
```

### macOS/Linux (MySQL):
```bash
# Install MySQL if needed
brew install mysql

# Start MySQL
mysql.server start

# Connect to MySQL
mysql -u root -p
```

## �📚 Sections Overview

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

## 📖 How to Use These Materials

### Learning Path (Recommended):

**Week 1: Foundation**
```
Day 1: Read database_design_concepts.py
Day 2: Run Create DB.sql
Day 3: Run Insert Data.sql & verify data
```

**Week 2: Basic Queries**
```
Day 1-2: Work through 02-DQL queries
Day 3: Practice writing your own queries
```

**Week 3: Advanced Queries**
```
Day 1-3: Work through 03-Advanced Queries
Day 4: Create your own complex queries
```

### Self-Paced Learning:
1. **Start**: Read sql_complete_guide.py for concepts
2. **Practice**: Run the provided SQL scripts
3. **Challenge**: Try modifying queries
4. **Create**: Write entirely new queries from scratch

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
10. **Experiment safely** - use INSERT/SELECT first, not DELETE on real data

## 🐛 Common Issues & How to Fix Them

### Issue 1: "Table does not exist"
```
✓ Solution: Make sure you ran Create DB.sql FIRST
✓ Check: Run "SELECT * FROM databases;" to see available databases
✓ If missing: Re-run Create DB.sql from 01- Create DB folder
```

### Issue 2: "Foreign key constraint failed"
```
✓ Reason: Inserting data with non-existent foreign key reference
✓ Solution: Run Insert Data.sql to populate all tables first
✓ Remember: Create parent tables BEFORE child tables
```

### Issue 3: "Column not found"
```
✓ Reason: Column name is case-sensitive or doesn't exist
✓ Solution: Check the Schema.png or run "DESCRIBE table_name;"
✓ Fix: Use exact column names from CREATE TABLE statements
```

### Issue 4: "Syntax Error near..."
```
✓ Check: Missing semicolon at end of statement
✓ Check: Quotes around string values ('text' not "text" in some systems)
✓ Check: Comma placement in SELECT lists
✓ Solution: Copy from provided scripts and modify carefully
```

### Issue 5: Query returns no results
```
✓ First: Verify data exists - SELECT COUNT(*) FROM table;
✓ Check: WHERE conditions might be too restrictive
✓ Try: Remove WHERE clause to see all records
✓ Debug: Add PRINT or ECHO statements to trace execution
```

### Issue 6: Database locked or in use
```
✓ Solution: Close other connections to the database
✓ Check: No other programs accessing the same database
✓ If persistent: Restart SQL Server or MySQL service
```

### Issue 7: Performance is slow
```
✓ For large datasets: Use LIMIT in queries (e.g., SELECT ... LIMIT 100;)
✓ Add: WHERE conditions to filter data before aggregation
✓ Structure: Write complex queries step-by-step
✓ Check indexes: Large tables benefit from indexed columns
```

## ✅ Success Checkpoints

You're progressing well when you can:
- ✓ Create tables with proper constraints without errors
- ✓ Insert data matching the schema structure
- ✓ Write SELECT queries that return expected results
- ✓ Join multiple tables and get correct results
- ✓ Use GROUP BY with aggregate functions
- ✓ Write subqueries that solve specific problems
- ✓ Modify data safely with UPDATE and DELETE
- ✓ Explain what each SQL statement does

## 🚨 Safety Practices

**Before running UPDATE or DELETE:**
```sql
-- 1. ALWAYS test your WHERE clause first
SELECT * FROM table_name WHERE condition;

-- 2. Only proceed if results are correct
UPDATE table_name SET column = value WHERE condition;

-- 3. Create backups before major operations
-- 4. Use transactions (BEGIN; ... COMMIT;)
```

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