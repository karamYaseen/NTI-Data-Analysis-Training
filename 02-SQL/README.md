# SQL — NTI practice

Personal coursework — **Karam Yaseen**. This folder holds DDL/DML scripts, basic DQL, and advanced query exercises, building on concepts from [`01-Database-Design/`](../01-Database-Design/README.md).

---

## Quick start

1. Open **[`01- Create DB & Insert Data/`](01-%20Create%20DB%20&%20Insert%20Data/)** — run `Create DB.sql`, then `Insert Data.sql`, in your SQL client.
2. Open **[`02- DQL/`](02-%20DQL/)** — use `SQLQuery2.sql` for starter `SELECT` examples.
3. Open **[`03- Advanced Queries/`](03-%20Advanced%20Queries/)** — joins, aggregates, and subqueries.

Rough effort for the whole folder: about **6–8 hours** (your pace may differ).

**Next:** [`../03-Python/README.md`](../03-Python/README.md) · **Parent:** [`../README.md`](../README.md)

---

## Prerequisites

**Knowledge:** Tables, primary and foreign keys, basic logical operators (from Database Design).

**Software:** A SQL client (e.g. SQL Server Management Studio, MySQL Workbench, Azure Data Studio) and a running database engine.

**Optional:** VS Code for editing; Git for version control.

---

## Environment notes

- **Windows (SQL Server):** Ensure the instance is running; connect with SSMS.
- **macOS/Linux (MySQL example):** Install and start the server, then `mysql -u root -p` (or your admin user).

Dialect-specific syntax (string quotes, `LIMIT` vs `TOP`) may require small edits to the provided scripts.

---

## Folder layout

```
02-SQL/
├── README.md
├── sql_complete_guide.py          # narrative reference (read alongside labs)
├── 01- Create DB & Insert Data/
│   ├── Create DB.sql
│   ├── Insert Data.sql
│   └── Schema.png
├── 02- DQL/
│   └── SQLQuery2.sql, SQLQuery3.sql
└── 03- Advanced Queries/
    └── SQLQuery1.sql
```

Each numbered subfolder has its own **README** with task detail.

---

## Suggested order

1. **[`01-Database-Design`](../01-Database-Design/)** — ERD and mapping context.
2. **`01- Create DB & Insert Data`** — create schema, load seed data, confirm structure.
3. **`02- DQL`** — filtering, sorting, simple retrieval.
4. **`03- Advanced Queries`** — JOINs, `GROUP BY`, subqueries, controlled updates.

Read **`sql_complete_guide.py`** for explanations of *why* the patterns work, not only *what* to type.

---

## Concepts at a glance

| Area | Topics |
|------|--------|
| DDL | `CREATE TABLE`, keys, constraints |
| DML | `INSERT`, `UPDATE`, `DELETE` |
| DQL | `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING`, subqueries, `UNION`, `EXISTS`, `CASE` |

The training schema typically includes employee, department, project, and assignment style tables (see `Schema.png` and subfolder READMEs).

---

## Tips

- Inspect the schema before writing multi-table queries.
- For `UPDATE`/`DELETE`, run the same filter in a `SELECT` first.
- Use aliases on joins for readability.
- Prefer transactions or backups before bulk changes on real data.

---

## Common issues

| Symptom | What to check |
|---------|----------------|
| Table does not exist | Database context correct? `Create DB.sql` executed successfully? |
| Foreign key error | Parent rows inserted first; follow DML order in `Insert Data.sql`. |
| Column not found | Exact column names from `CREATE TABLE`; case sensitivity by engine. |
| Empty result set | Relax `WHERE` conditions; verify rows exist with `COUNT(*)`. |
| Syntax error | Semicolons, commas in `SELECT` lists, string quoting for your dialect. |

---

## Example patterns

```sql
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id;
```

```sql
SELECT e.first_name, e.last_name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_no = d.dept_no;
```

```sql
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

## Author

Karam Yaseen — personal coursework, not an official NTI release.
