# Database Design Fundamentals

This section contains comprehensive database design materials covering Entity-Relationship Diagrams (ERD), normalization, and relational mapping concepts.

## Prerequisites

- Understand tables, keys, and simple relationships
- Can read diagrams

## Topics Covered

- ERD fundamentals: entities, attributes, relationships, cardinality
- Normalization (1NF–3NF) to reduce redundancy
- Mapping ER models to tables (1:1, 1:N, N:M)
- Four case studies: Musicana, Real‑Estate, Hospital, Airline

## Project Structure

- `database_design_concepts.py` – detailed concepts
- `01-ERD/` – four problem folders with diagrams
- `02-Mapping/` – corresponding relational schemas

Each problem folder includes a README and image.

## ERD Overview

- **Musicana**: musicians, instruments, albums, songs (many-to-many links)
- **Real Estate**: properties, owners, agents, sales
- **Hospital**: patients, doctors, departments, treatments
- **Airline**: flights, passengers, aircraft, airports

## Mapping Problems Overview

Each mapping problem converts the corresponding ERD into:
- Relational tables with proper keys
- Foreign key relationships
- Normalized schema (1NF, 2NF, 3NF)
- SQL table creation scripts

## How to Use

1. Read the concepts file.
2. Pick a problem, draw ERD, then check solution.
3. Map ERD to tables and compare.
4. Repeat; work alone or with peers.

#### Tips

    - Start ERD with entities, then add relationships
    - Normalize to 3NF but don’t overthink it
    - Draw first, map later
    - Avoid redundant attributes and missing relations
    

## Related Resources

These materials lead to:
- **SQL Module** (../02-SQL/): Implement these designs using SQL

## Tools and Technologies

- **ERD Design**: Mermaid, Draw.io
- **Documentation**: Markdown, GitHub


## Author
Karam Yaseen
