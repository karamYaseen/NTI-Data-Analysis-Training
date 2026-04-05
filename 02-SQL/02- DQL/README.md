# SQL — DQL — my basic queries

**My NTI coursework** — **Karam Yaseen.** **My** first query drills: `SELECT`, `WHERE`, simple joins — **how I** practiced pulling and filtering data.

## What I practiced here

**I** worked on:
- Write basic SELECT statements
- Filter data with WHERE clauses
- Use comparison and logical operators
- Create column aliases
- Calculate derived values
- Access related data through simple joins

## Files in this folder

- `README.md` - This documentation (with explanation and guidance)
- `SQLQuery2.sql` - Solution queries for basic tasks
- `SQLQuery3.sql` - Alternative implementations and examples

## Basic queries exercise (Tasks 1–9)

These introductory queries teach fundamental SQL skills using single-table and simple multi-table operations.

### Task 1: Display all the employees Data
**Objective**: Retrieve complete employee records
**Concept**: Basic SELECT with all columns
```
SELECT * FROM Employees;
```
**Key Learning**: 
- `*` means all columns
- Returns all employee records

---

### Task 2: Display employee First name, last name, Salary and Department number
**Objective**: Retrieve specific columns
**Concept**: Column selection and projection
```
SELECT FirstName, LastName, Salary, DeptNo FROM Employees;
```
**Key Learning**:
- Specify only needed columns
- Improves query performance
- More readable results

---

### Task 3: Display all the projects names, locations and the department which is responsible about it
**Objective**: Retrieve project information
**Concept**: Selecting from different tables
```
SELECT ProjectName, ProjectLocation, DeptNo FROM Projects;
```
**Key Learning**:
- Different tables store different information
- Query the appropriate table for needed data

---

### Task 4: Display each employee full name and his annual commission (10% of annual salary)
**Objective**: Calculate derived values
**Concept**: Expressions in SELECT and column aliasing
```
SELECT 
    FirstName + ' ' + LastName AS FullName,
    (Salary * 12 * 0.10) AS ANNUAL_COMM
FROM Employees;
```
**Key Learning**:
- Perform calculations in SELECT
- Use aliases (AS) for meaningful column names
- String concatenation for derived data
- Column aliases make results clearer

---

### Task 5: Display employees with salary > 1000 LE monthly
**Objective**: Filter records with conditions
**Concept**: WHERE clause with comparison operators
```
SELECT EmpID, FirstName, LastName, Salary
FROM Employees
WHERE Salary > 1000;
```
**Key Learning**:
- WHERE clause filters rows
- Returns only rows meeting the condition
- Comparison operators: >, <, >=, <=, =, !=

---

### Task 6: Display employees earning more than 10000 LE annually
**Objective**: Filter using calculated values
**Concept**: WHERE clause with expressions
```
SELECT EmpID, FirstName + ' ' + LastName AS FullName, Salary * 12
FROM Employees
WHERE Salary * 12 > 10000;
```
**Key Learning**:
- Can use calculations in WHERE clause
- Annual salary = monthly salary * 12
- Filters applied before results displayed

---

### Task 7: Display names and salaries of female employees
**Objective**: Filter by categorical data
**Concept**: WHERE clause with text/string values
```
SELECT FirstName, LastName, Salary, Gender
FROM Employees
WHERE Gender = 'F';
```
**Key Learning**:
- String values use single quotes
- Single = for comparison (not ==)
- Useful for demographic filtering

---

### Task 8: Display department managed by manager ID 968574
**Objective**: Locate specific manager's department
**Concept**: Filtering by ID values
```
SELECT DeptID, DeptName, MgrSSN
FROM Departments
WHERE MgrSSN = 968574;
```
**Key Learning**:
- Find relationships between tables
- Manager SSN links to Employees table
- Useful for organizational queries

---

### Task 9: Display IDs, names, and locations of projects controlled by department 10
**Objective**: Find related records
**Concept**: Filtering related data
```
SELECT ProjectID, ProjectName, ProjectLocation, DeptNo
FROM Projects
WHERE DeptNo = 10;
```
**Key Learning**:
- Projects are controlled by departments
- Department number links Projects to Departments table
- Filtering finds related records

---

## Key concepts for basic queries

### SELECT Statement Structure
```
SELECT    [columns to display]
FROM      [table name]
WHERE     [conditions to filter]
ORDER BY  [sorting preference]
```

### Data Types & Comparisons
| Data Type | Example Values | Operators |
|-----------|----------------|-----------|
| Numbers | 1000, 3.14, -50 | =, !=, <, >, <=, >= |
| Text | 'Ahmed', 'Cairo' | = (exact match), LIKE (pattern) |
| Dates | '2023-01-15' | =, <, >, BETWEEN |
| Boolean | Male/Female, Yes/No | = exact match |

### Column Aliases
```
SELECT column_name AS alias_name FROM table;
```
Benefits:
- Makes column headers more readable
- Required for calculated columns
- Helps with complex queries

### String Concatenation
Combine text columns:
```
SELECT FirstName + ' ' + LastName AS FullName
-- or
SELECT CONCAT(FirstName, ' ', LastName) AS FullName
-- or (MySQL)
SELECT CONCAT_WS(' ', FirstName, LastName) AS FullName
```

### Expressions in SELECT
Calculate values on the fly:
```
SELECT 
    ProductPrice,
    Quantity,
    ProductPrice * Quantity AS TotalPrice,
    (ProductPrice * Quantity * 0.1) AS TaxAmount
FROM Orders;
```

### NULL Values
- NULL means "unknown" or "not applicable"
- Filter for NULL: `WHERE column IS NULL`
- Filter out NULL: `WHERE column IS NOT NULL`

## Difficulty progression

1. **Very Easy**: Tasks 1, 2, 3 (Simple column selection)
2. **Easy**: Tasks 5, 8, 9 (Basic WHERE filtering)
3. **Medium**: Tasks 4, 6, 7 (Expressions and calculations)

## Expected results

After completing these tasks, you'll be comfortable with:
- Writing SELECT statements
- Filtering with WHERE clauses
- Creating meaningful column aliases
- Calculating derived values
- Comparing different data types
- Building blocks for complex queries

## Related concepts (learn next)

These basic queries lead to more complex patterns:
- **JOIN operations**: Combine data from multiple tables formally
- **GROUP BY**: Aggregate data by categories
- **ORDER BY**: Sort results in meaningful ways
- **Aggregate functions**: COUNT, SUM, AVG, MIN, MAX
- **Subqueries**: Nested queries for complex filtering

## Best practices

1. **Always specify columns** - Avoid SELECT * in production
2. **Use meaningful aliases** - Make your data understandable
3. **Write readable code** - Use line breaks for clarity
4. **Test incrementally** - Build complex queries step by step
5. **Use WHERE wisely** - Filter early to reduce data processed
6. **Comment your queries** - Explain the purpose

## Common mistakes to avoid

| Mistake | Wrong | Correct |
|---------|-------|---------|
| Wrong operator | WHERE Salary = > 1000 | WHERE Salary > 1000 |
| Missing quotes | WHERE Gender = F | WHERE Gender = 'F' |
| Using AND when needed OR | Or/And | WHERE dept = 30 AND dept = 20 | WHERE dept IN (30, 20) |
| Forgetting alias | SALARY * 12 | `SALARY * 12 AS AnnualSalary` |

## SQL execution tips

1. **Execute once** - Run each query separately to check results
2. **Compare results** - Check if output matches expectations
3. **Debug WHERE clause** - Remove it to see all data, then add conditions
4. **Use meaningful names** - Column aliases improve understanding
5. **Document findings** - Note insights from query results

**Parent:** [`../README.md`](../README.md) · **Previous:** [`../01- Create DB & Insert Data/README.md`](../01-%20Create%20DB%20&%20Insert%20Data/README.md) · **Next:** [`../03- Advanced Queries/README.md`](../03-%20Advanced%20Queries/README.md)

## Author

Karam Yaseen

---

**Level:** beginner · **Time:** ~2–3 hours · **Prerequisite:** schema from Create DB section · **Last updated:** April 2026
