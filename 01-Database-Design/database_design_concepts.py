# Database Design Fundamentals
# This file covers Entity-Relationship Diagrams (ERD), normalization, and mapping concepts

# ===========================================
# ENTITY-RELATIONSHIP DIAGRAMS (ERD)
# ===========================================

# ERD Components:
# - Entities: Objects or concepts (rectangles)
# - Attributes: Properties of entities (ellipses)
# - Relationships: Associations between entities (diamonds)
# - Cardinality: How many instances relate (1:1, 1:N, N:M)

# ===========================================
# ENTITIES AND ATTRIBUTES
# ===========================================

# Entity: A real-world object or concept
# Examples: Customer, Product, Order, Employee

# Attributes: Properties that describe an entity
# - Simple attributes: Single value (Name, Age, Price)
# - Composite attributes: Multiple components (Address: Street, City, State, Zip)
# - Derived attributes: Calculated from other attributes (Age from BirthDate)
# - Multi-valued attributes: Multiple values (Phone Numbers, Skills)

# ===========================================
# RELATIONSHIPS
# ===========================================

# Relationship Types:
# - One-to-One (1:1): Each entity instance relates to one other instance
#   Example: Employee has one EmployeeID, EmployeeID belongs to one Employee

# - One-to-Many (1:N): One entity instance relates to many other instances
#   Example: Customer places many Orders, Order belongs to one Customer

# - Many-to-Many (N:M): Many instances relate to many other instances
#   Example: Student enrolls in many Courses, Course has many Students

# ===========================================
# KEYS
# ===========================================

# Primary Key: Unique identifier for each entity instance
# - Must be unique
# - Cannot be null
# - Should not change over time

# Foreign Key: Attribute that references primary key of another entity
# - Establishes relationships between entities
# - Can be null (optional relationship)
# - Must match referenced primary key value

# ===========================================
# NORMALIZATION
# ===========================================

# First Normal Form (1NF):
# - Eliminate repeating groups
# - Each attribute contains atomic values
# - Each record is unique

# Second Normal Form (2NF):
# - Must be in 1NF
# - Remove partial dependencies
# - Non-key attributes depend on entire primary key

# Third Normal Form (3NF):
# - Must be in 2NF
# - Remove transitive dependencies
# - Non-key attributes depend only on primary key

# ===========================================
# RELATIONAL MAPPING
# ===========================================

# 1:1 Relationship Mapping:
# - Primary key of one entity becomes foreign key in other
# - Or create separate table with both primary keys

# 1:N Relationship Mapping:
# - Primary key of "1" side becomes foreign key in "N" side

# N:M Relationship Mapping:
# - Create junction/associative table
# - Include primary keys of both entities as composite primary key
# - Can include additional attributes (relationship attributes)

# ===========================================
# PRACTICAL EXAMPLES
# ===========================================

# Example 1: Musicana Records Database
# Entities: Musician, Instrument, Album, Song
# Relationships:
# - Musician plays Instrument (N:M)
# - Album contains Song (1:N)
# - Song performed by Musician (N:M)
# - Musician produces Album (1:N)

# Example 2: Real Estate Firm
# Entities: Property, Owner, Agent, Sale
# Relationships:
# - Owner owns Property (1:N)
# - Agent sells Property (N:M)
# - Sale involves Property, Owner, Agent (associative entity)

# Example 3: Hospital Management
# Entities: Patient, Doctor, Department, Treatment
# Relationships:
# - Doctor works in Department (N:1)
# - Patient treated by Doctor (N:M)
# - Treatment involves Patient and Doctor (associative entity)

# Example 4: Airline Company
# Entities: Flight, Passenger, Aircraft, Airport
# Relationships:
# - Flight uses Aircraft (N:1)
# - Flight departs from/arrives at Airport (N:1)
# - Passenger books Flight (N:M)