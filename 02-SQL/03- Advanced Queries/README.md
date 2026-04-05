# Advanced SQL — my deeper queries

**My NTI coursework** — **Karam Yaseen.** **My** stretch work: JOINs, aggregates, subqueries, trickier filters — **my** solutions in `SQLQuery1.sql`.

## What I practiced here

**I** worked on:
- Combine data from multiple tables using JOINs
- Aggregate and group data by categories
- Write nested queries (subqueries)
- Use advanced filtering techniques
- Solve complex real-world data problems

## Files in this folder

- `README.md` - This documentation (with detailed explanations)
- `SQLQuery1.sql` - Solution queries for advanced tasks

## Advanced query concepts

### 1. JOINs - Combining Multiple Tables

The most powerful SQL feature is combining data from multiple related tables.

#### Types of JOINs:

**INNER JOIN** - Returns only matching rows from both tables
```sql
SELECT e.FirstName, e.LastName, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptNo = d.DeptNo;
```
- Returns employees that have a department
- Only rows with valid department references

**LEFT JOIN (LEFT OUTER JOIN)** - All rows from left table + matching from right
```sql
SELECT e.FirstName, e.LastName, d.DeptName
FROM Employees e
LEFT JOIN Departments d ON e.DeptNo = d.DeptNo;
```
- Returns all employees, even without department
- Department name is NULL if employee has no department

**RIGHT JOIN (RIGHT OUTER JOIN)** - Matching rows from left + all from right
```sql
SELECT e.FirstName, d.DeptName
FROM Employees e
RIGHT JOIN Departments d ON e.DeptNo = d.DeptNo;
```
- Returns all departments, even without employees
- Employee names are NULL if department has no employees

**FULL OUTER JOIN** - All rows from both tables
```sql
SELECT e.FirstName, d.DeptName
FROM Employees e
FULL OUTER JOIN Departments d ON e.DeptNo = d.DeptNo;
```
- Returns all employees and all departments
- Either can have NULL values if no match

#### JOIN Condition:
The ON clause specifies how to match rows:
```sql
ON e.DeptNo = d.DeptNo  -- Match when dept numbers are equal
```
This creates the relationship between tables.

#### Multiple JOINs:
You can join many tables together:
```sql
SELECT e.FirstName, d.DeptName, p.ProjectName, wo.Hours
FROM Employees e
INNER JOIN Departments d ON e.DeptNo = d.DeptNo
INNER JOIN Works_On wo ON e.EmpSSN = wo.EmpSSN
INNER JOIN Projects p ON wo.ProjectNo = p.ProjectNo;
```
This shows employees, their departments, the projects they work on, and hours worked.

### 2. AGGREGATE FUNCTIONS - Summarizing Data

Aggregate functions combine multiple rows into a single result.

#### Common Functions:

**COUNT()** - Counts rows
```sql
SELECT COUNT(*) FROM Employees;           -- Total employees
SELECT COUNT(DISTINCT DeptNo) FROM Employees;  -- Unique departments
SELECT COUNT(SupervisorSSN) FROM Employees;    -- Non-NULL values
```

**SUM()** - Adds numeric values
```sql
SELECT SUM(Salary) FROM Employees;        -- Total salary expenses
```

**AVG()** - Calculates average
```sql
SELECT AVG(Salary) FROM Employees;        -- Average salary
```

**MIN() / MAX()** - Minimum and maximum values
```sql
SELECT MIN(Salary), MAX(Salary) FROM Employees;
```

### 3. GROUP BY - Aggregating by Categories

GROUP BY groups rows by one or more columns, then applies aggregate functions.

#### Basic GROUP BY:
```sql
SELECT DeptNo, COUNT(*) as EmployeeCount
FROM Employees
GROUP BY DeptNo;
```
Shows count of employees per department.

#### Multiple Columns:
```sql
SELECT DeptNo, Gender, COUNT(*) as Count
FROM Employees
GROUP BY DeptNo, Gender;
```
Shows employee count by department and gender.

#### With Calculations:
```sql
SELECT DeptNo, AVG(Salary) as AvgSalary
FROM Employees
GROUP BY DeptNo;
```
Shows average salary per department.

#### HAVING Clause:
Filters results AFTER grouping (while WHERE filters BEFORE grouping):
```sql
SELECT DeptNo, AVG(Salary) as AvgSalary
FROM Employees
GROUP BY DeptNo
HAVING AVG(Salary) > 50000;
```
Shows only departments with average salary > $50,000.

### 4. SUBQUERIES - Nested Queries

Subqueries are queries within queries, used for complex filtering.

#### Subquery in WHERE Clause:
```sql
SELECT * FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```
Shows employees earning more than average.

#### Subquery in FROM Clause:
```sql
SELECT dept_summary.*
FROM (
    SELECT DeptNo, COUNT(*) as EmpCount, AVG(Salary) as AvgSal
    FROM Employees
    GROUP BY DeptNo
) AS dept_summary
WHERE dept_summary.EmpCount > 5;
```
Creates a temporary table with department summaries, then filters.

#### Correlated Subquery:
References outer query's columns:
```sql
SELECT e1.FirstName, e1.Salary
FROM Employees e1
WHERE Salary > (
    SELECT AVG(e2.Salary)
    FROM Employees e2
    WHERE e2.DeptNo = e1.DeptNo
);
```
Shows employees earning more than their department's average.

### 5. EXISTS - Checking for Related Records

EXISTS checks if a subquery returns any rows.

```sql
SELECT DeptName FROM Departments d
WHERE EXISTS (
    SELECT 1 FROM Employees e
    WHERE e.DeptNo = d.DeptNo
);
```
Shows only departments that have employees.

### 6. IN Operator - Multiple Values

IN checks if a value matches any in a list.

```sql
SELECT * FROM Projects
WHERE DeptNo IN (10, 20, 30);
```
Shows projects in departments 10, 20, or 30.

### 7. Set Operations - UNION

UNION combines results from multiple queries.

```sql
SELECT FirstName, LastName FROM Employees
UNION
SELECT Name FROM Managers;
```
Combines employee and manager names.

**UNION vs UNION ALL:**
- UNION: Removes duplicates
- UNION ALL: Keeps duplicates (faster)

### 8. CASE - Conditional Logic

CASE adds if-then-else logic to queries.

```sql
SELECT 
    FirstName,
    Salary,
    CASE
        WHEN Salary < 40000 THEN 'Entry Level'
        WHEN Salary < 60000 THEN 'Mid Level'
        WHEN Salary < 80000 THEN 'Senior'
        ELSE 'Management'
    END AS SalaryLevel
FROM Employees;
```
Categorizes each employee by salary range.

## Example advanced queries

### Example 1: Department Summary Report
```sql
SELECT 
    d.DeptName,
    COUNT(e.EmpSSN) as EmployeeCount,
    AVG(e.Salary) as AvgSalary,
    MAX(e.Salary) as MaxSalary,
    MIN(e.Salary) as MinSalary
FROM Departments d
LEFT JOIN Employees e ON d.DeptNo = e.DeptNo
GROUP BY d.DeptNo, d.DeptName
ORDER BY AvgSalary DESC;
```
Shows salary statistics for each department.

### Example 2: Employees on Multiple Projects
```sql
SELECT 
    e.FirstName,
    e.LastName,
    COUNT(DISTINCT wo.ProjectNo) as ProjectCount,
    SUM(wo.Hours) as TotalHours
FROM Employees e
LEFT JOIN Works_On wo ON e.EmpSSN = wo.EmpSSN
GROUP BY e.EmpSSN, e.FirstName, e.LastName
HAVING COUNT(DISTINCT wo.ProjectNo) > 1
ORDER BY TotalHours DESC;
```
Shows employees working on multiple projects ranked by hours.

### Example 3: Find Highest Paid in Each Department
```sql
SELECT DISTINCT
    d.DeptName,
    e.FirstName,
    e.LastName,
    e.Salary
FROM Departments d
INNER JOIN Employees e ON d.DeptNo = e.DeptNo
WHERE e.Salary = (
    SELECT MAX(Salary)
    FROM Employees
    WHERE DeptNo = d.DeptNo
);
```
Shows the highest-paid employee in each department.

## Key patterns

### Pattern 1: Find Missing Data
```sql
SELECT d.DeptName
FROM Departments d
LEFT JOIN Employees e ON d.DeptNo = e.DeptNo
WHERE e.EmpSSN IS NULL;
```
Shows departments with no employees.

### Pattern 2: Compare to Aggregate
```sql
SELECT 
    FirstName,
    Salary,
    AVG(Salary) OVER (PARTITION BY DeptNo) as DeptAvg
FROM Employees;
```
Shows each employee's salary vs department average.

### Pattern 3: Rank Within Group
```sql
SELECT 
    FirstName,
    DeptNo,
    Salary,
    ROW_NUMBER() OVER (PARTITION BY DeptNo ORDER BY Salary DESC) as Rank
FROM Employees;
```
Ranks employees by salary within their department.

## Common advanced query mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Wrong JOIN type | Missing data or duplicates | Verify which JOIN you need |
| Forgetting GROUP BY | "Column not aggregated" error | Include all non-aggregate columns |
| Using WHERE instead of HAVING | Filtering before grouping | Use HAVING for grouped filters |
| Wrong subquery | Invalid results | Test subquery independently first |
| Missing parentheses | Syntax error | GROUP parentheses around subqueries |

## Tips for writing advanced queries

1. **Start Simple** - Build complex queries step by step
2. **Test Components** - Test JOINs before adding aggregates
3. **Check Data Types** - Ensure columns being joined are same type
4. **Use Aliases** - Make complex queries readable
5. **Document Logic** - Add comments explaining the purpose
6. **Verify Results** - Check record counts and sample data

## Query building steps

1. **Identify needed tables** - What data do you need?
2. **Determine relationships** - How do tables connect?
3. **Choose JOIN type** - Inner, Left, Right, or Full?
4. **Add conditions** - WHERE clause filters
5. **Add aggregation** - GROUP BY and aggregate functions
6. **Filter groups** - HAVING clause
7. **Sort results** - ORDER BY clause
8. **Limit output** - LIMIT clause if needed

## What you'll learn

After completing advanced queries, you'll understand:
- How to efficiently combine multiple tables
- How to aggregate and summarize data
- How to solve complex data problems
- How to write optimized queries
- How to analyze business data effectively

## Best practices

1. **Always use aliases** for table names in JOINs
2. **Test WHERE conditions** before using with aggregates
3. **Use DISTINCT cautiously** - can be expensive
4. **Consider performance** - not all correct queries are fast
5. **Comment complex logic** - future you will thank you
6. **Backup before modifying data** - UPDATE/DELETE are permanent

## Related advanced topics

Once comfortable with these concepts, explore:
- **Window Functions** - PARTITION BY, ROW_NUMBER(), RANK()
- **Stored Procedures** - Reusable query collections
- **Triggers** - Automatic actions on data changes
- **Views** - Virtual tables from query results
- **Indexes** - Query performance optimization
- **Transactions** - Multi-step atomic operations

**Parent:** [`../README.md`](../README.md) · **Previous:** [`../02- DQL/README.md`](../02-%20DQL/README.md) · **Next track:** [`../../03-Python/README.md`](../../03-Python/README.md)

## Author

Karam Yaseen

---

**Level:** advanced · **Time:** ~4–6 hours · **Prerequisite:** DQL section · **Last updated:** April 2026
