# Database Design Fundamentals

This section contains comprehensive database design materials covering Entity-Relationship Diagrams (ERD), normalization, and relational mapping concepts.

## 🚀 Quick Start

**New to Database Design?** Follow this path:
1. Read [database_design_concepts.py](database_design_concepts.py) for theoretical foundation
2. Start with **Problem 1: Musicana Records** (simplest)
3. Review both the ERD and Mapping for each problem
4. Progress to more complex problems (2, 3, 4)

**Expected Time**: 2-3 hours to complete and understand all 4 problems

## 📚 Prerequisites & Knowledge Required

- Basic understanding of **data structures and relationships**
- Familiar with **basic database concepts** (tables, records, fields)
- Able to **read and interpret visual diagrams**
- *Optional*: Experience with relational databases or SQL

## Topics Covered

### 1. Entity-Relationship Diagrams (ERD)
Conceptual database design methodology:
- **Entities**: Objects or concepts that need to be stored
  - Strong entities vs weak entities
  - Entity identification and naming
- **Attributes**: Properties that describe entities
  - Simple, composite, derived, and multi-valued attributes
  - Key attributes and constraints
- **Relationships**: Associations between entities
  - One-to-One (1:1), One-to-Many (1:N), Many-to-Many (N:M)
  - Cardinality and participation constraints
  - Relationship attributes

### 2. Database Normalization
Ensuring data integrity and eliminating redundancy:
- **First Normal Form (1NF)**: Eliminate repeating groups
  - Atomic values and unique records
  - Primary key identification
- **Second Normal Form (2NF)**: Remove partial dependencies
  - Full functional dependency on primary key
  - Non-key attribute dependencies
- **Third Normal Form (3NF)**: Remove transitive dependencies
  - Direct dependencies on primary key only
  - Transitive dependency elimination

### 3. Relational Mapping
Converting ERD to relational database schema:
- **1:1 Relationship Mapping**: Foreign key placement strategies
- **1:N Relationship Mapping**: Foreign key in "many" side
- **N:M Relationship Mapping**: Junction/associative tables
- **Weak Entity Mapping**: Identifying relationships
- **Multivalued Attribute Mapping**: Separate tables

### 4. Practical Case Studies
Real-world database design problems:
- **Musicana Records**: Musicians, instruments, albums, songs
- **Real Estate Firm**: Properties, owners, agents, sales
- **General Hospital**: Patients, doctors, departments, treatments
- **Airline Company**: Flights, passengers, aircraft, airports

## Project Structure

```
01-Database-Design/
├── README.md                           # This documentation file
├── database_design_concepts.py         # Comprehensive concepts guide
├── ERD/                               # Entity-Relationship Diagrams
│   ├── Problem1_Musicana/
│   │   ├── README.md                  # Problem description
│   │   └── Musican.png               # ERD diagram
│   ├── Problem2_RealEstate/
│   │   ├── README.md
│   │   └── RealEstate.png
│   ├── Problem3_Hospital/
│   │   ├── README.md
│   │   └── Hospital.png
│   └── Problem4_Airline/
│       ├── README.md
│       └── AirLine.png
└── Mapping/                           # Relational Mapping
    ├── Problem 1 Musicana Records/
    │   ├── README.md
    │   └── Musicana Records.png
    ├── Problem 2 Real Estate Firm/
    │   ├── README.md
    │   └── Real Estate Firm.png
    ├── Problem 3 General Hospital/
    │   ├── README.md
    │   └── General Hospital.png
    └── Problem 4 Airline Company/
        ├── README.md
        ├── Airline Company.png
        ├── Lab4.docx
        └── Ps.txt
```

## ERD Problems Overview

### Problem 1: Musicana Records
**Entities**: Musician, Instrument, Album, Song
**Key Relationships**:
- Musician plays Instrument (N:M)
- Album contains Song (1:N)
- Song performed by Musician (N:M)
- Musician produces Album (1:N)

### Problem 2: Real Estate Firm
**Entities**: Property, Owner, Agent, Sale
**Key Relationships**:
- Owner owns Property (1:N)
- Agent sells Property (N:M)
- Sale transaction linking all entities

### Problem 3: General Hospital
**Entities**: Patient, Doctor, Department, Treatment
**Key Relationships**:
- Doctor works in Department (N:1)
- Patient treated by Doctor (N:M)
- Treatment records with associative data

### Problem 4: Airline Company
**Entities**: Flight, Passenger, Aircraft, Airport
**Key Relationships**:
- Flight uses Aircraft (N:1)
- Flight connects Airports (departure/arrival)
- Passenger books Flight (N:M)

## Mapping Problems Overview

Each mapping problem converts the corresponding ERD into:
- Relational tables with proper keys
- Foreign key relationships
- Normalized schema (1NF, 2NF, 3NF)
- SQL table creation scripts

## Learning Objectives

After completing this section, you should be able to:
- Design Entity-Relationship Diagrams for real-world scenarios
- Identify entities, attributes, and relationships
- Apply normalization principles to eliminate data redundancy
- Convert ERD to relational database schema
- Understand cardinality and participation constraints
- Create well-structured database designs

## 📖 How to Use These Materials

### For Self-Study:
1. **Study the Concepts**
   - Read `database_design_concepts.py` to understand theory
   - Reference this README for key concepts

2. **Work Through Problems**
   - Each problem folder has both ERD and Mapping subfolders
   - ERD folder: Visual design of entities and relationships
   - Mapping folder: Conversion to relational schema
   
3. **Practice & Verify**
   - Try creating your own ERD before viewing the solution
   - Compare your mapping with the provided one
   - Understand WHY the mapping is structured that way

### For Group Learning:
1. Discuss each problem as a team
2. Draw ERDs together before viewing solutions
3. Debate the best normalization approach
4. Present mappings to the group

## 💡 Best Practices & Tips

### When Creating ERDs:
- **Start with entities**: Identify all objects/nouns first
- **Define attributes**: List all properties for each entity
- **Identify relationships**: Show how entities interact
- **Mark cardinality**: Clearly show 1:1, 1:N, N:M relationships
- **Specify participation**: Indicate if participation is total or partial

### When Normalizing:
- **Check 1NF**: Ensure atomic values in all columns
- **Check 2NF**: Remove partial dependencies on composite keys
- **Check 3NF**: Remove transitive dependencies
- **Document decisions**: Why did you normalize this way?
- **Avoid over-normalization**: Balance between structure and query efficiency

### Common Mistakes to Avoid:
- ❌ Starting mapping before finalizing ERD
- ❌ Missing relationships between entities
- ❌ Creating redundant attributes
- ❌ Using poor naming conventions
- ❌ Ignoring normalization (causes data anomalies)

## ✅ Success Indicators

You understand Database Design when you can:
- ✓ Identify all entities in a business requirement
- ✓ Determine correct relationships and cardinality
- ✓ Normalize a schema to 3NF without losing information
- ✓ Explain your design decisions clearly
- ✓ Convert between ER model and relational schema

## 🎯 Practice Workflow

For each problem:

```
1. Read the problem description (each Problem folder has README.md)
   ↓
2. Create your own ERD based on the requirements
   ↓
3. View the provided ERD - Compare with yours
   ↓
4. Create your own mapping/normalization
   ↓
5. View the provided mapping - Compare with yours
   ↓
6. Identify differences and understand why
   ↓
7. Move to next problem with increased complexity
```

## 🔗 Related Resources

These materials lead to:
- **SQL Module** (../02-SQL/): Implement these designs using SQL
- **Data Modeling**: Work with actual databases
- **Database Administration**: Manage and optimize designs

## Tools and Technologies

- **ERD Design**: Mermaid, Draw.io, Lucidchart
- **Database Management**: MySQL, PostgreSQL, SQLite
- **Documentation**: Markdown, GitHub

## Author
Karam Yaseen