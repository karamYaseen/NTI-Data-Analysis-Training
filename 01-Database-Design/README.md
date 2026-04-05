# Database Design Fundamentals

**My NTI coursework** — **Karam Yaseen.** This folder holds **my** ERD and mapping work (Musicana, Real Estate, Hospital, Airline): **how I** practiced entities, relationships, cardinality, and normalization (through 3NF). It is **my** study archive, not a generic textbook.

---

## What I already had in mind

- Basic tables / PK / FK ideas  
- I could read simple diagrams (and picked up Mermaid / draw.io as **I** went)

---

## Topics covered

- ERD basics: entities, attributes, relationships, cardinality  
- Normalization (1NF–3NF) to cut redundancy and update anomalies  
- Mapping ER models to tables (1:1, 1:N, M:N)  
- Case studies: **Musicana**, **Real Estate**, **Hospital**, **Airline**

---

## Folder layout

| Path | Purpose |
|------|---------|
| `database_design_concepts.py` | Narrative concepts and examples (read alongside problems) |
| `01-ERD/` | One folder per problem — task statement + **my** ERD |
| `02-Mapping/` | **My** map from ERD → tables, keys, relationships |

Each problem folder has a **README** (and often diagram files).

---

## Case studies (short)

- **Musicana:** musicians, instruments, albums, songs (several M:N relationships)  
- **Real Estate:** properties, owners, agents, sales  
- **Hospital:** patients, staff, departments, treatments  
- **Airline:** flights, passengers, aircraft, airports  

---

## What I aimed to produce (mapping)

For each case **I** tried to deliver:

- Tables with primary and foreign keys  
- Relationship lines matching cardinality  
- Schema in **third normal form** where it made sense for me  
- Optional: `CREATE TABLE` scripts when I moved into [`../02-SQL/`](../02-SQL/)

---

## How I used this folder

1. Skim `database_design_concepts.py`.  
2. Open **01-ERD** for a problem; sketch **my** ERD (paper, draw.io, or Mermaid).  
3. Open **02-Mapping** for the same problem; write **my** tables and keys.  
4. Compare with class solutions when I had them; iterate **my** way.

**What worked for me**

- Entities first, then relationships and cardinalities.  
- 3NF as a target without over-normalizing toy examples.  
- ERD on paper before table lists.  
- Watch for missing entities, weak M:N handling, redundant attributes.

---

## What I did next

**[`../02-SQL/`](../02-SQL/)** — where **I** turned designs into DDL/DML and queries.

---

## Tools

- **Diagrams:** Mermaid, [draw.io](https://app.diagrams.net/)  
- **Docs:** Markdown (this repo)

**Parent:** [`../README.md`](../README.md)

**Author:** Karam Yaseen — personal coursework, **my** way.
