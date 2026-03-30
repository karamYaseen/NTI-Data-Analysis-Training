# Python Data Analysis — Complete Tutorial with Code Examples
#
# How to run:  cd 03-Python   then   python tutorial.py
# (Outputs: PNG/CSV/XLSX in this folder; see ../.gitignore for ignored patterns.)
#
# This file contains the entire course curriculum with detailed explanations,
# code examples, and progressive learning from basics to advanced automation.

# =============================================================================
# COURSE OVERVIEW
# =============================================================================
"""
NTI Data Analysis Training — Python Section
Duration: 5 days + 1 recap session
Goal: Master Python for data analysis and automation
Technologies: Python, NumPy, Pandas, Matplotlib, SQL Server, Web Scraping

WHAT YOU'LL LEARN:
- Day 1: Python fundamentals (variables, types, collections)
- Day 2: Control flow and advanced data structures
- Day 3: Functions and object-oriented programming
- Day 4: Data analysis with NumPy, Pandas, Matplotlib
- Session 7: Advanced automation (SQL, scraping, regex, pipelines)

KEY CONCEPTS:
- Functions: Reusable code blocks
- OOP: Classes, inheritance, encapsulation
- Data Analysis: Arrays, DataFrames, visualization
- Automation: SQL integration, web scraping, regex, Excel handling
"""

# =============================================================================
# DAY 1: PYTHON FUNDAMENTALS
# =============================================================================
"""
Day 1 focuses on basic Python syntax, data types, and simple operations.
You'll learn how Python handles variables, basic data structures, and I/O.
"""

# -----------------------------------------------------------------------------
# 1.1 BASIC SYNTAX & DATA TYPES
# -----------------------------------------------------------------------------
"""
Python uses indentation for code blocks. No semicolons needed!
Variables store data and can change types dynamically.
"""

# Variables and types
name = "Alice"        # String (text)
age = 25             # Integer (whole number)
height = 5.7         # Float (decimal number)
is_student = True    # Boolean (True/False)

# Print output with f-strings (formatted strings)
print("=== DAY 1: BASICS ===")
print(f"Hello, {name}! You are {age} years old.")
print(f"Height: {height} feet, Student: {is_student}")

# Basic operations
print(f"Age next year: {age + 1}")
print(f"Height in cm: {height * 30.48}")

# -----------------------------------------------------------------------------
# 1.2 LISTS, TUPLES, AND BASIC OPERATIONS
# -----------------------------------------------------------------------------
"""
Collections store multiple values.
Lists are mutable (can be changed), tuples are immutable (cannot be changed).
"""

# List (mutable collection)
fruits = ["apple", "banana", "orange"]
print(f"\nOriginal fruits: {fruits}")

# Modify list
fruits.append("grape")     # Add item
fruits[0] = "pineapple"    # Change first item
print(f"Modified fruits: {fruits}")

# Tuple (immutable collection)
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
# coordinates[0] = 15  # This would cause an error!

# Basic list operations
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Length: {len(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

# -----------------------------------------------------------------------------
# 1.3 STRINGS AND STRING OPERATIONS
# -----------------------------------------------------------------------------
"""
Strings are sequences of characters. Python has powerful string methods.
"""

message = "Hello, World!"
print(f"\nString: {message}")
print(f"Upper: {message.upper()}")
print(f"Lower: {message.lower()}")
print(f"Length: {len(message)}")
print(f"Replace: {message.replace('World', 'Python')}")

# String formatting
name = "Alice"
age = 25
greeting = f"My name is {name} and I am {age} years old."
print(f"Formatted: {greeting}")

# -----------------------------------------------------------------------------
# 1.4 DICTIONARIES (KEY-VALUE PAIRS)
# -----------------------------------------------------------------------------
"""
Dictionaries store data as key-value pairs. Very fast lookups.
"""

# Create dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": True
}

print(f"\nDictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Modify dictionary
person["age"] = 26
person["job"] = "Engineer"
print(f"Updated: {person}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# =============================================================================
# DAY 2: CONTROL FLOW & ADVANCED DATA STRUCTURES
# =============================================================================
"""
Day 2 covers decision-making, loops, and complex data structures.
You'll learn how to control program execution flow.
"""

# -----------------------------------------------------------------------------
# 2.1 CONDITIONAL STATEMENTS (IF-ELIF-ELSE)
# -----------------------------------------------------------------------------
"""
Make decisions in code based on conditions.
"""

print("\n=== DAY 2: CONTROL FLOW ===")

age = 18
if age >= 18:
    print("You can vote!")
elif age >= 16:
    print("You can drive!")
else:
    print("You're too young for both.")

# Multiple conditions
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} = Grade {grade}")

# -----------------------------------------------------------------------------
# 2.2 LOOPS (FOR AND WHILE)
# -----------------------------------------------------------------------------
"""
Repeat actions using loops.
"""

# For loop with list
fruits = ["apple", "banana", "orange"]
print("\nFor loop with fruits:")
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with range
print("\nCounting with range:")
for i in range(1, 6):
    print(f"Count: {i}")

# While loop
count = 0
print("\nWhile loop:")
while count < 3:
    print(f"Count: {count}")
    count += 1

# Loop with break and continue
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nEven numbers only:")
for num in numbers:
    if num % 2 != 0:  # Skip odd numbers
        continue
    if num > 8:       # Stop at 8
        break
    print(num)

# -----------------------------------------------------------------------------
# 2.3 SETS (UNIQUE VALUES)
# -----------------------------------------------------------------------------
"""
Sets store unique values. No duplicates allowed.
"""

# Create set
unique_numbers = {1, 2, 2, 3, 3, 3}
print(f"\nSet (removes duplicates): {unique_numbers}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# -----------------------------------------------------------------------------
# 2.4 EXCEPTION HANDLING
# -----------------------------------------------------------------------------
"""
Handle errors gracefully instead of crashing.
"""

print("\nException handling:")

# Basic try-except
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    number = int("abc")
except ValueError:
    print("Cannot convert 'abc' to integer!")
except TypeError:
    print("Type error occurred!")

# Finally block (always executes)
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs (cleanup code)")

# -----------------------------------------------------------------------------
# 2.5 LIST COMPREHENSIONS
# -----------------------------------------------------------------------------
"""
Create lists in a concise way.
"""

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"\nList comprehension - squares: {squares}")

# With condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in numbers}
print(f"Dictionary comprehension: {squares_dict}")

# =============================================================================
# DAY 3: FUNCTIONS & OBJECT-ORIENTED PROGRAMMING
# =============================================================================
"""
Day 3 covers reusable code with functions and modeling with classes.
Functions organize code, OOP models real-world entities.
"""

print("\n=== DAY 3: FUNCTIONS & OOP ===")

# -----------------------------------------------------------------------------
# 3.1 FUNCTIONS BASICS
# -----------------------------------------------------------------------------
"""
Functions are reusable blocks of code that perform specific tasks.
Benefits: reusability, modularity, maintainability, readability, testing.
"""

def greet_person(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

# Call the function
message = greet_person("Alice")
print(f"Function result: {message}")

def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width

area = calculate_area(5, 3)
print(f"Rectangle area: {area}")

# -----------------------------------------------------------------------------
# 3.2 FUNCTION PARAMETERS
# -----------------------------------------------------------------------------
"""
Different types of parameters: positional, default, keyword, *args, **kwargs.
"""

# Default parameters
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))                    # Uses default message
print(greet("Bob", "Good morning"))      # Overrides default

# Keyword arguments
def create_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

print(create_person(name="Alice", age=25, city="NYC"))
print(create_person(city="LA", name="Bob", age=30))  # Order doesn't matter

# *args (variable positional arguments)
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1-10: {sum_all(*range(1, 11))}")  # Unpack range

# **kwargs (variable keyword arguments)
def print_info(**info):
    """Print key-value information."""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# -----------------------------------------------------------------------------
# 3.3 LAMBDA FUNCTIONS
# -----------------------------------------------------------------------------
"""
Anonymous functions for simple operations.
"""

# Basic lambda
square = lambda x: x ** 2
print(f"Lambda square: {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"Lambda add: {add(3, 4)}")

# Lambda in sorting
names = ["Alice", "Bob", "Charlie", "David"]
names.sort(key=lambda name: len(name))  # Sort by length
print(f"Sorted by length: {names}")

# -----------------------------------------------------------------------------
# 3.4 CLASSES AND OBJECTS
# -----------------------------------------------------------------------------
"""
Classes are blueprints for objects. Objects are instances of classes.
"""

class Car:
    """A simple Car class."""

    def __init__(self, make, model, year):
        """Initialize a Car object."""
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        """Start the car's engine."""
        return f"The {self.year} {self.make} {self.model} starts!"

    def get_description(self):
        """Get car description."""
        return f"{self.year} {self.make} {self.model}"

# Create objects (instances)
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)

print(f"Car 1: {car1.get_description()}")
print(f"Car 2: {car2.get_description()}")
print(f"Start car 1: {car1.start_engine()}")

# -----------------------------------------------------------------------------
# 3.5 INHERITANCE
# -----------------------------------------------------------------------------
"""
Inheritance allows classes to inherit properties and methods from parent classes.
"""

class ElectricCar(Car):
    """An electric car that inherits from Car."""

    def __init__(self, make, model, year, battery_range):
        """Initialize ElectricCar with additional battery info."""
        super().__init__(make, model, year)  # Call parent constructor
        self.battery_range = battery_range

    def charge(self):
        """Charge the electric car."""
        return f"Charging the {self.make} {self.model}..."

    def get_description(self):
        """Override parent method to include battery info."""
        base_desc = super().get_description()
        return f"{base_desc} (Range: {self.battery_range} miles)"

tesla = ElectricCar("Tesla", "Model 3", 2023, 300)
print(f"Tesla: {tesla.get_description()}")
print(f"Charge: {tesla.charge()}")
print(f"Start: {tesla.start_engine()}")  # Inherited method

# -----------------------------------------------------------------------------
# 3.7 ADVANCED FUNCTION CONCEPTS: SCOPE AND CLOSURES
# -----------------------------------------------------------------------------
"""
Advanced function features for complex programming patterns.
"""

# Global vs Local scope
global_var = "I'm global!"

def demonstrate_scope():
    """Show how scope works in Python."""
    local_var = "I'm local!"
    print(f"Inside function: {local_var}")  # Local variable
    print(f"Inside function (global): {globals()['global_var']}")  # Access global explicitly

    # Local shadows global if same name
    local_global_var = "Local shadow!"  # This creates a local variable
    print(f"Inside function (local): {local_global_var}")

demonstrate_scope()
print(f"Outside function: {global_var}")  # Original global unchanged

# Using global keyword to modify global variables
def modify_global():
    """Modify a global variable from inside a function."""
    global global_var
    global_var = "Modified by function!"
    print(f"Inside function: {global_var}")

modify_global()
print(f"After modification: {global_var}")

# -----------------------------------------------------------------------------
# 3.8 PARAMETER PASSING: MUTABLE VS IMMUTABLE
# -----------------------------------------------------------------------------
"""
Understanding how Python passes arguments to functions.
"""

def modify_immutable(x):
    """Immutable objects (numbers, strings) create new objects."""
    print(f"Before: {x}, id: {id(x)}")
    x = x + 1  # Creates new object
    print(f"After: {x}, id: {id(x)}")  # Different id

def modify_mutable(lst):
    """Mutable objects (lists, dicts) are modified in place."""
    print(f"Before: {lst}, id: {id(lst)}")
    lst.append(4)  # Modifies original object
    print(f"After: {lst}, id: {id(lst)}")  # Same id

num = 5
my_list = [1, 2, 3]

modify_immutable(num)  # num unchanged outside function
print(f"Original num: {num}")

modify_mutable(my_list)  # my_list modified outside function
print(f"Original list: {my_list}")

# -----------------------------------------------------------------------------
# 3.9 HIGHER-ORDER FUNCTIONS AND CLOSURES
# -----------------------------------------------------------------------------
"""
Functions that work with other functions and capture variables from enclosing scope.
"""

# Higher-order functions: functions as arguments
def apply_operation(func, numbers):
    """Apply a function to each number in a list."""
    return [func(num) for num in numbers]

# Closures: functions that capture variables from enclosing scope
def create_multiplier(factor):
    """Return a function that multiplies by a specific factor."""
    def multiplier(x):
        return x * factor  # Captures 'factor' from enclosing scope
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# -----------------------------------------------------------------------------
# 3.10 COMPREHENSIVE DOCSTRINGS
# -----------------------------------------------------------------------------
"""
Professional documentation for functions.
"""

def calculate_statistics(numbers):
    """
    Calculate basic statistics for a list of numbers.

    This function demonstrates comprehensive docstring documentation
    following Google/NumPy style conventions.

    Parameters:
    -----------
    numbers : list of float or int
        A list of numerical values to analyze

    Returns:
    --------
    dict
        Dictionary containing statistical measures:
        - 'mean': arithmetic mean
        - 'median': middle value when sorted
        - 'std': standard deviation
        - 'min': minimum value
        - 'max': maximum value

    Raises:
    -------
    ValueError
        If input list is empty or contains non-numeric values

    Examples:
    ---------
    >>> stats = calculate_statistics([1, 2, 3, 4, 5])
    >>> print(stats['mean'])
    3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate statistics for empty list")

    try:
        import statistics
        return {
            'mean': statistics.mean(numbers),
            'median': statistics.median(numbers),
            'std': statistics.stdev(numbers),
            'min': min(numbers),
            'max': max(numbers)
        }
    except statistics.StatisticsError:
        raise ValueError("Invalid numeric data")

# Test the function
try:
    stats = calculate_statistics([1, 2, 3, 4, 5])
    print(f"Statistics: {stats}")
except ValueError as e:
    print(f"Error: {e}")

# -----------------------------------------------------------------------------
# 3.11 PRACTICAL FUNCTION EXAMPLES
# -----------------------------------------------------------------------------
"""
Real-world function patterns you'll use frequently.
"""

def get_high_salary_employees(employees, min_salary=50000):
    """
    Filter employees by minimum salary.

    Parameters:
    -----------
    employees : list of dict
        List of employee dictionaries with 'name' and 'salary' keys
    min_salary : float
        Minimum salary threshold

    Returns:
    --------
    list of dict
        Filtered list of high-salary employees
    """
    return [emp for emp in employees if emp['salary'] >= min_salary]

# Test data
employee_data = [
    {'name': 'Alice', 'salary': 75000},
    {'name': 'Bob', 'salary': 45000},
    {'name': 'Charlie', 'salary': 80000},
    {'name': 'Diana', 'salary': 55000}
]

high_salary = get_high_salary_employees(employee_data, 60000)
print(f"High salary employees: {[emp['name'] for emp in high_salary]}")

# FizzBuzz function (common coding interview problem)
def fizz_buzz(n):
    """Return Fizz, Buzz, FizzBuzz, or the number based on divisibility rules."""
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Generate FizzBuzz sequence
fizzbuzz_results = [fizz_buzz(i) for i in range(1, 16)]
print(f"FizzBuzz 1-15: {fizzbuzz_results}")

# String reversal function
def reverse_string(text):
    """Reverse a string using slicing."""
    return text[::-1]

print(f"Reverse 'hello': {reverse_string('hello')}")

# =============================================================================
# ADVANCED OOP CONCEPTS
# =============================================================================

# -----------------------------------------------------------------------------
# 3.12 PROPERTIES WITH VALIDATION
# -----------------------------------------------------------------------------
"""
Using properties to validate data before setting attributes.
"""

class ValidatedDog:
    """A dog class with validated name property."""

    def __init__(self, name, age):
        self.name = name  # Uses setter validation
        self.age = age

    @property
    def name(self):
        """Get the dog's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the dog's name with validation."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not value.replace(' ', '').isalpha():
            raise ValueError("Name must contain only letters and spaces")
        if len(value.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self._name = value.strip().title()

    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"

# Test validation
try:
    dog1 = ValidatedDog("Buddy", 3)
    print(f"Created: {dog1}")

    dog1.name = "Max"  # Valid
    print(f"Renamed: {dog1}")

    # dog1.name = "123"  # Would raise ValueError
    # dog1.name = "A"    # Would raise ValueError

except ValueError as e:
    print(f"Validation error: {e}")

# -----------------------------------------------------------------------------
# 3.13 STRING REPRESENTATION METHODS
# -----------------------------------------------------------------------------
"""
Custom string representations for objects.
"""

class BankAccount:
    """A bank account with custom string representations."""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        """User-friendly string representation."""
        return f"Account owned by {self.owner} with balance ${self.balance:,.2f}"

    def __repr__(self):
        """Developer-friendly representation for debugging."""
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

account = BankAccount("Alice Johnson", 1250.50)
print(f"str(): {str(account)}")
print(f"repr(): {repr(account)}")

# -----------------------------------------------------------------------------
# 3.14 OPERATOR OVERLOADING
# -----------------------------------------------------------------------------
"""
Define how operators work with custom objects.
"""

class Vector:
    """A 2D vector with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Subtract two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        """Multiply vector by scalar."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __eq__(self, other):
        """Check if two vectors are equal."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Test operator overloading
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v2 - v1: {v2 - v1}")
print(f"v1 * 3: {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(1, 2): {v1 == Vector(1, 2)}")

# -----------------------------------------------------------------------------
# 3.15 ENCAPSULATION WITH PRIVATE ATTRIBUTES
# -----------------------------------------------------------------------------
"""
Hide internal implementation details using private attributes.
"""

class SecureAccount:
    """A bank account with private attributes."""

    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance  # Private attribute
        self.__pin = pin          # Private attribute

    def get_balance(self, pin):
        """Get balance with PIN verification."""
        if self.__verify_pin(pin):
            return self.__balance
        else:
            raise ValueError("Invalid PIN")

    def deposit(self, amount, pin):
        """Deposit money with PIN verification."""
        if self.__verify_pin(pin):
            if amount > 0:
                self.__balance += amount
                return f"Deposited ${amount}. New balance: ${self.__balance}"
            else:
                raise ValueError("Deposit amount must be positive")
        else:
            raise ValueError("Invalid PIN")

    def __verify_pin(self, pin):
        """Private method to verify PIN."""
        return self.__pin == pin

# Test encapsulation
account = SecureAccount("Alice", 1000, "1234")

try:
    print(f"Balance: ${account.get_balance('1234')}")
    print(account.deposit(500, "1234"))
    print(f"New balance: ${account.get_balance('1234')}")

    # Try with wrong PIN
    # account.get_balance("0000")  # Would raise ValueError

except ValueError as e:
    print(f"Error: {e}")

# Note: Private attributes can still be accessed with name mangling
# print(account._SecureAccount__balance)  # Not recommended!

# =============================================================================
# DAY 4: DATA ANALYSIS WITH NUMPY, PANDAS & MATPLOTLIB
# =============================================================================
"""
Day 4 covers numerical computing, data manipulation, and visualization.
NumPy for arrays, Pandas for DataFrames, Matplotlib for plots.
"""

print("\n=== DAY 4: DATA ANALYSIS ===")

# -----------------------------------------------------------------------------
# 4.1 NUMPY ARRAYS
# -----------------------------------------------------------------------------
"""
NumPy provides fast, efficient arrays for numerical computing.
Why NumPy? Memory-efficient, vectorized operations, rich math functions.
"""

import numpy as np

# Create arrays
numbers = np.array([1, 2, 3, 4, 5])
print(f"NumPy array: {numbers}")
print(f"Type: {type(numbers)}")
print(f"Shape: {numbers.shape}")

# Vectorized operations (element-wise)
print(f"Multiply by 2: {numbers * 2}")
print(f"Square: {numbers ** 2}")
print(f"Add 10: {numbers + 10}")

# 2D arrays (matrices)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D array:\n{matrix}")
print(f"Shape: {matrix.shape}")

# Array operations
print(f"Sum: {numbers.sum()}")
print(f"Mean: {numbers.mean()}")
print(f"Standard deviation: {numbers.std()}")
print(f"Max: {numbers.max()}, Min: {numbers.min()}")

# Indexing and slicing
print(f"First element: {numbers[0]}")
print(f"Last three: {numbers[-3:]}")
print(f"Matrix row 0: {matrix[0]}")
print(f"Matrix element [1,2]: {matrix[1, 2]}")

# -----------------------------------------------------------------------------
# 4.2 PANDAS DATAFRAMES
# -----------------------------------------------------------------------------
"""
Pandas provides DataFrames for tabular data manipulation.
Like Excel but programmable and scalable.
"""

import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', 'Miami'],
    'Salary': [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print(f"\nPandas DataFrame:\n{df}")

# Basic inspection
print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Data types:\n{df.dtypes}")

# Selection
print(f"\nFirst 2 rows:\n{df.head(2)}")
print(f"Name column: {df['Name'].tolist()}")
print(f"Alice's data:\n{df[df['Name'] == 'Alice']}")

# Filtering
high_salary = df[df['Salary'] > 55000]
print(f"\nHigh salary people:\n{high_salary}")

# Adding columns
df['Bonus'] = df['Salary'] * 0.1
print(f"\nWith bonus column:\n{df}")

# -----------------------------------------------------------------------------
# 4.3 DATA CLEANING WITH PANDAS
# -----------------------------------------------------------------------------
"""
Real-world data often needs cleaning: missing values, duplicates, formatting.
"""

# Create messy data
messy_data = {
    'Name': ['Alice', 'Bob', None, 'Diana', 'Alice'],
    'Age': [25, None, 35, 28, 25],
    'City': ['NYC', 'LA', 'Chicago', None, 'NYC'],
    'Salary': [50000, 60000, 70000, 55000, 50000]
}

df_messy = pd.DataFrame(messy_data)
print(f"\nMessy data:\n{df_messy}")

# Handle missing values
print(f"\nMissing values:\n{df_messy.isnull().sum()}")
df_clean = df_messy.dropna()  # Remove rows with NaN
print(f"\nAfter dropna:\n{df_clean}")

# Fill missing values
df_filled = df_messy.fillna({'Name': 'Unknown', 'Age': df_messy['Age'].mean(), 'City': 'Unknown'})
print(f"\nAfter fillna:\n{df_filled}")

# Remove duplicates
df_no_dupes = df_messy.drop_duplicates()
print(f"\nAfter drop_duplicates:\n{df_no_dupes}")

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')
print(f"\nClean column names: {list(df.columns)}")

# -----------------------------------------------------------------------------
# 4.4 GROUPING AND AGGREGATION
# -----------------------------------------------------------------------------
"""
Group data by categories and compute statistics.
"""

# Sample sales data
sales_data = {
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Clothing', 'Electronics', 'Books', 'Electronics'],
    'Sales': [100, 200, 150, 50, 250, 120, 80, 180]
}

df_sales = pd.DataFrame(sales_data)
print(f"\nSales data:\n{df_sales}")

# Group by category
grouped = df_sales.groupby('Category')
print(f"\nSales by category:\n{grouped['Sales'].sum()}")

# Multiple aggregations
agg_results = grouped['Sales'].agg(['sum', 'mean', 'count'])
print(f"\nAggregations:\n{agg_results}")

# Group by multiple columns
product_category = df_sales.groupby(['Category', 'Product'])['Sales'].sum()
print(f"\nBy category and product:\n{product_category}")

# -----------------------------------------------------------------------------
# 4.5 MERGING DATAFRAMES
# -----------------------------------------------------------------------------
"""
Combine data from multiple DataFrames.
"""

# Employee data
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'dept_id': [1, 2, 1, 3]
})

# Department data
departments = pd.DataFrame({
    'dept_id': [1, 2, 3],
    'dept_name': ['Engineering', 'Sales', 'HR'],
    'location': ['NYC', 'LA', 'Chicago']
})

print(f"\nEmployees:\n{employees}")
print(f"\nDepartments:\n{departments}")

# Left join
merged = pd.merge(employees, departments, on='dept_id', how='left')
print(f"\nMerged (left join):\n{merged}")

# -----------------------------------------------------------------------------
# 4.6 MATPLOTLIB VISUALIZATION
# -----------------------------------------------------------------------------
"""
Create charts and graphs to visualize data.
"""

import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o', color='blue', linestyle='--')
plt.title('Line Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)

# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 17, 32]
plt.subplot(2, 2, 2)
plt.bar(categories, values, color='green', alpha=0.7)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Scatter plot
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
plt.subplot(2, 2, 3)
plt.scatter(x_scatter, y_scatter, alpha=0.6)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Histogram
data_hist = np.random.normal(0, 1, 1000)
plt.subplot(2, 2, 4)
plt.hist(data_hist, bins=30, alpha=0.7, color='red')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# -----------------------------------------------------------------------------
# 4.7 ADVANCED NUMPY OPERATIONS
# -----------------------------------------------------------------------------
"""
More sophisticated NumPy operations for complex data processing.
"""

# Random array generation
random_array = np.random.rand(3, 3)  # Uniform random [0, 1)
print(f"\nRandom array:\n{random_array}")

# Random integers
random_ints = np.random.randint(1, 100, size=(2, 5))
print(f"Random integers:\n{random_ints}")

# Normal distribution
normal_data = np.random.normal(0, 1, 1000)  # Mean=0, std=1
print(f"Normal distribution sample: {normal_data[:10]}...")

# Advanced indexing and boolean masking
data = np.arange(1, 21).reshape(4, 5)
print(f"\nOriginal data:\n{data}")

# Boolean indexing
mask = data > 10
print(f"Values > 10: {data[mask]}")

# Conditional replacement
data[data % 2 == 0] = -1  # Replace even numbers with -1
print(f"After replacing evens with -1:\n{data}")

# -----------------------------------------------------------------------------
# 4.8 ADVANCED PANDAS OPERATIONS
# -----------------------------------------------------------------------------
"""
Professional Pandas techniques for data manipulation.
"""

# Create more complex sample data
sales_data = {
    'Date': pd.date_range('2023-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Sales': np.random.uniform(100, 1000, 100),
    'Quantity': np.random.randint(1, 20, 100)
}

df_sales = pd.DataFrame(sales_data)
print(f"\nSales DataFrame:\n{df_sales.head()}")

# Comprehensive data inspection
print(f"\nDataFrame Info:")
print(f"Shape: {df_sales.shape}")
print(f"Columns: {list(df_sales.columns)}")
print(f"Data types:\n{df_sales.dtypes}")
print(f"Missing values:\n{df_sales.isnull().sum()}")
print(f"Summary statistics:\n{df_sales.describe()}")

# Advanced filtering
high_sales = df_sales[
    (df_sales['Sales'] > 500) &
    (df_sales['Region'].isin(['North', 'East']))
]
print(f"\nHigh sales in North/East:\n{high_sales.head()}")

# String operations
df_sales['Product_Code'] = df_sales['Product'].str.lower() + '_prod'
print(f"\nWith product codes:\n{df_sales[['Product', 'Product_Code']].head()}")

# Date operations
df_sales['Month'] = df_sales['Date'].dt.month
df_sales['Year'] = df_sales['Date'].dt.year
df_sales['DayOfWeek'] = df_sales['Date'].dt.day_name()

print(f"\nWith date components:\n{df_sales[['Date', 'Month', 'Year', 'DayOfWeek']].head()}")

# Advanced grouping
monthly_sales = df_sales.groupby(['Year', 'Month'])['Sales'].agg(['sum', 'mean', 'count'])
print(f"\nMonthly sales summary:\n{monthly_sales}")

# Pivot tables
pivot_sales = df_sales.pivot_table(
    values='Sales',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
print(f"\nSales pivot table:\n{pivot_sales}")

# -----------------------------------------------------------------------------
# 4.9 ADVANCED MATPLOTLIB VISUALIZATION
# -----------------------------------------------------------------------------
"""
Professional plotting techniques with multiple subplots and customization.
"""

# Create sample data for visualization
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Advanced Matplotlib Visualization', fontsize=16, fontweight='bold')

# Line plots with customization
axes[0, 0].plot(x, y1, 'b-', linewidth=2, label='sin(x)', alpha=0.8)
axes[0, 0].plot(x, y2, 'r--', linewidth=2, label='cos(x)', alpha=0.8)
axes[0, 0].set_title('Trigonometric Functions')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('y')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Scatter plot with color mapping
colors = np.random.rand(50)
sizes = np.random.rand(50) * 1000
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)

scatter = axes[0, 1].scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6, cmap='viridis')
axes[0, 1].set_title('Scatter Plot with Size & Color')
axes[0, 1].set_xlabel('X values')
axes[0, 1].set_ylabel('Y values')
plt.colorbar(scatter, ax=axes[0, 1], label='Color intensity')

# Bar chart with error bars
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
errors = [2, 3, 4, 3, 2]

bars = axes[1, 0].bar(categories, values, yerr=errors, capsize=5,
                      color=['skyblue', 'lightgreen', 'lightcoral', 'gold', 'violet'],
                      alpha=0.7)
axes[1, 0].set_title('Bar Chart with Error Bars')
axes[1, 0].set_xlabel('Categories')
axes[1, 0].set_ylabel('Values')

# Add value labels on bars
for bar, value in zip(bars, values):
    axes[1, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{value}', ha='center', va='bottom')

# Histogram with multiple datasets
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1.5, 1000)

axes[1, 1].hist(data1, bins=30, alpha=0.7, label='Dataset 1', color='blue', density=True)
axes[1, 1].hist(data2, bins=30, alpha=0.7, label='Dataset 2', color='red', density=True)
axes[1, 1].set_title('Overlapping Histograms')
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Density')
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('tutorial_advanced_plots.png', dpi=150, bbox_inches='tight')
print("\nAdvanced plots saved as 'tutorial_advanced_plots.png'")

# =============================================================================
# SESSION 7: ADVANCED AUTOMATION
# =============================================================================
"""
Session 7 combines SQL, web scraping, regex, and Excel automation.
Build end-to-end data pipelines.
"""

print("\n=== SESSION 7: ADVANCED AUTOMATION ===")

# -----------------------------------------------------------------------------
# 7.1 SQL SERVER INTEGRATION
# -----------------------------------------------------------------------------
"""
Connect Python to SQL Server for database operations.
"""

# Note: This section requires SQL Server setup
# import pyodbc

# Example connection (commented out - requires SQL Server)
"""
cs = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=company;Trusted_Connection=yes;"
conn = pyodbc.connect(cs)
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE employees (
        id INT PRIMARY KEY,
        name NVARCHAR(255),
        salary FLOAT
    )
''')

# Insert data
employees_data = [(1, "Alice", 50000), (2, "Bob", 60000)]
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?)", employees_data)
conn.commit()

# Query data
df_sql = pd.read_sql("SELECT * FROM employees", conn)
print(f"SQL data:\n{df_sql}")

conn.close()
"""

print("SQL integration: Requires SQL Server setup (see LAUNCH.md)")

# -----------------------------------------------------------------------------
# 7.2 WEB SCRAPING
# -----------------------------------------------------------------------------
"""
Extract data from websites automatically.
"""

import requests
from bs4 import BeautifulSoup

# Example scraping (using a safe, public site)
url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    scraped_data = []
    for quote in quotes[:5]:  # First 5 quotes
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        scraped_data.append({"quote": text, "author": author})

    df_scraped = pd.DataFrame(scraped_data)
    print(f"\nScraped quotes:\n{df_scraped.head()}")

    # Save to CSV
    df_scraped.to_csv('tutorial_scraped_quotes.csv', index=False)
    print("Scraped data saved to 'tutorial_scraped_quotes.csv'")

except Exception as e:
    print(f"Scraping example skipped: {e}")

# -----------------------------------------------------------------------------
# 7.3 REGULAR EXPRESSIONS
# -----------------------------------------------------------------------------
"""
Pattern-based text processing and extraction.
"""

import re

# Sample text for regex
sample_text = """
Contact information:
- Email: john.doe@example.com
- Phone: (555) 123-4567
- Website: https://www.example.com
- Another email: jane_smith@test.org
- Numbers: 42, 3.14, 1000
- Dates: 2023-12-25, 01/15/2024
"""

print(f"\nSample text:\n{sample_text}")

# Find emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, sample_text)
print(f"Emails found: {emails}")

# Find phone numbers (simple pattern)
phone_pattern = r"\(\d{3}\) \d{3}-\d{4}"
phones = re.findall(phone_pattern, sample_text)
print(f"Phones found: {phones}")

# Find numbers
number_pattern = r"\d+\.?\d*"
numbers = re.findall(number_pattern, sample_text)
print(f"Numbers found: {numbers}")

# Find dates
date_pattern = r"\d{4}-\d{2}-\d{2}"
dates = re.findall(date_pattern, sample_text)
print(f"Dates found: {dates}")

# -----------------------------------------------------------------------------
# 7.4 EXCEL AUTOMATION
# -----------------------------------------------------------------------------
"""
Programmatic Excel file handling.
"""

# Create sample data
excel_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [1200, 25, 75, 300],
    'Stock': [50, 200, 150, 30],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics']
}

df_excel = pd.DataFrame(excel_data)
print(f"\nExcel data:\n{df_excel}")

# Save to Excel
df_excel.to_excel('tutorial_products.xlsx', index=False, sheet_name='Products')
print("Data saved to 'tutorial_products.xlsx'")

# Read back and analyze
df_read = pd.read_excel('tutorial_products.xlsx')
print(f"\nRead back:\n{df_read}")

# Analysis
total_value = (df_read['Price'] * df_read['Stock']).sum()
print(f"Total inventory value: ${total_value:,.2f}")

by_category = df_read.groupby('Category')['Price'].mean()
print(f"Average price by category:\n{by_category}")

# -----------------------------------------------------------------------------
# 7.5 COMPLETE PIPELINE EXAMPLE
# -----------------------------------------------------------------------------
"""
Combine multiple technologies into an automated workflow.
"""

def create_sample_data():
    """Create sample employee data."""
    return pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
        'salary': [75000, 65000, 80000, 60000, 70000],
        'experience': [3, 5, 7, 4, 6]
    })

def process_data(df):
    """Process and analyze the data."""
    # Add bonus column
    df['bonus'] = df['salary'] * 0.1

    # Calculate total compensation
    df['total_comp'] = df['salary'] + df['bonus']

    # Group by department
    dept_summary = df.groupby('department').agg({
        'salary': 'mean',
        'bonus': 'sum',
        'total_comp': 'sum'
    }).round(2)

    return df, dept_summary

def generate_report(processed_df, summary_df):
    """Generate a comprehensive report."""
    report = f"""
EMPLOYEE COMPENSATION REPORT
{'='*50}

INDIVIDUAL EMPLOYEE DATA:
{processed_df.to_string(index=False)}

DEPARTMENT SUMMARY:
{summary_df.to_string()}

KEY METRICS:
- Total employees: {len(processed_df)}
- Average salary: ${processed_df['salary'].mean():,.2f}
- Total bonuses: ${processed_df['bonus'].sum():,.2f}
- Total compensation: ${processed_df['total_comp'].sum():,.2f}
"""
    return report

# Run the pipeline
print("\n" + "="*60)
print("COMPLETE DATA PIPELINE EXAMPLE")
print("="*60)

# Step 1: Create data
raw_data = create_sample_data()
print("Step 1: Sample data created")

# Step 2: Process data
processed_data, summary = process_data(raw_data)
print("Step 2: Data processed and analyzed")

# Step 3: Generate report
report = generate_report(processed_data, summary)
print("Step 3: Report generated")

# Step 4: Save outputs
processed_data.to_csv('tutorial_employee_data.csv', index=False)
summary.to_excel('tutorial_department_summary.xlsx', index=True)

with open('tutorial_compensation_report.txt', 'w') as f:
    f.write(report)

print("Step 4: All outputs saved")
print("Files created:")
print("- tutorial_employee_data.csv")
print("- tutorial_department_summary.xlsx")
print("- tutorial_compensation_report.txt")

# -----------------------------------------------------------------------------
# 7.6 SQL SERVER INTEGRATION WITH PYODBC
# -----------------------------------------------------------------------------
"""
Connect Python to SQL Server for database operations.
Note: Requires SQL Server installation and pyodbc package.
"""

# Example connection (requires SQL Server setup)
# import pyodbc
# import os

# Connection string for SQL Server
# connection_string = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=localhost\\SQLEXPRESS;"
#     "DATABASE=company;"
#     "Trusted_Connection=yes;"
# )

# def get_database_connection():
#     """Establish database connection with error handling."""
#     try:
#         conn = pyodbc.connect(connection_string, timeout=10)
#         print("Database connection successful")
#         return conn
#     except pyodbc.Error as e:
#         print(f"Database connection failed: {e}")
#         return None

# Create sample data for demonstration
sample_employee_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Eve Wilson'],
    'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
    'salary': [75000, 65000, 80000, 60000, 70000],
    'hire_date': ['2020-01-15', '2019-03-20', '2018-11-10', '2021-05-05', '2019-08-30']
})

print(f"\nSample employee data for SQL demo:\n{sample_employee_data}")

# Example SQL operations (commented out - requires database)
"""
# Create table
def create_employee_table(conn):
    create_query = '''
    CREATE TABLE employees (
        id INT PRIMARY KEY,
        name NVARCHAR(255) NOT NULL,
        department NVARCHAR(100),
        salary FLOAT,
        hire_date DATE
    )
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(create_query)
        conn.commit()
        print("Employee table created successfully")
    except pyodbc.Error as e:
        print(f"Error creating table: {e}")

# Insert data
def insert_employee_data(conn, df):
    insert_query = '''
    INSERT INTO employees (id, name, department, salary, hire_date)
    VALUES (?, ?, ?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute(insert_query, (
                row['id'], row['name'], row['department'],
                row['salary'], row['hire_date']
            ))
        conn.commit()
        print(f"Inserted {len(df)} employee records")
    except pyodbc.Error as e:
        print(f"Error inserting data: {e}")

# Query with parameters
def get_high_salary_employees(conn, min_salary=70000):
    query = '''
    SELECT id, name, department, salary
    FROM employees
    WHERE salary > ?
    ORDER BY salary DESC
    '''
    try:
        df = pd.read_sql(query, conn, params=(min_salary,))
        return df
    except pyodbc.Error as e:
        print(f"Error querying data: {e}")
        return pd.DataFrame()

# Example usage:
# conn = get_database_connection()
# if conn:
#     create_employee_table(conn)
#     insert_employee_data(conn, sample_employee_data)
#     high_salary_df = get_high_salary_employees(conn, 65000)
#     print(f"High salary employees:\n{high_salary_df}")
#     conn.close()
"""

print("SQL integration: Requires SQL Server setup (see installation guide)")

# -----------------------------------------------------------------------------
# 7.7 ADVANCED WEB SCRAPING PATTERNS
# -----------------------------------------------------------------------------
"""
Professional web scraping with error handling and best practices.
"""

def scrape_quotes_with_error_handling():
    """Scrape quotes with comprehensive error handling."""
    import time

    url = "https://quotes.toscrape.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        print("Fetching quotes from web...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise exception for bad status codes

        soup = BeautifulSoup(response.text, "html.parser")

        quotes_data = []
        quote_elements = soup.find_all("div", class_="quote")

        for quote in quote_elements[:10]:  # Limit to 10 quotes
            try:
                text = quote.find("span", class_="text").get_text(strip=True)
                author = quote.find("small", class_="author").get_text(strip=True)
                tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

                quotes_data.append({
                    'quote': text,
                    'author': author,
                    'tags': ', '.join(tags)
                })

            except AttributeError as e:
                print(f"Error parsing quote: {e}")
                continue

        df_quotes = pd.DataFrame(quotes_data)
        print(f"Successfully scraped {len(df_quotes)} quotes")

        # Save with timestamp
        timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
        filename = f'tutorial_quotes_{timestamp}.csv'
        df_quotes.to_csv(filename, index=False)
        print(f"Quotes saved to '{filename}'")

        return df_quotes

    except requests.RequestException as e:
        print(f"Network error: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()

# Run scraping example
scraped_quotes = scrape_quotes_with_error_handling()
if not scraped_quotes.empty:
    print(f"\nSample scraped quotes:\n{scraped_quotes.head()}")

# -----------------------------------------------------------------------------
# 7.8 ADVANCED REGULAR EXPRESSIONS
# -----------------------------------------------------------------------------
"""
Complex pattern matching for data extraction and validation.
"""

# Sample text for regex demonstration
sample_text = """
Employee Records:
- John Doe (john.doe@company.com) - Phone: (555) 123-4567 - ID: EMP001
- Jane Smith (jane_smith@test.org) - Phone: 555-987-6543 - ID: EMP002
- Bob Johnson (bob.johnson@startup.net) - Phone: (555) 456-7890 - ID: EMP003

Financial Data:
Total revenue: $1,234,567.89
Expenses: $987,654.32
Profit margin: 23.45%

Dates found: 2023-12-25, 01/15/2024, 2024-02-14
IP addresses: 192.168.1.1, 10.0.0.1, 172.16.0.1
URLs: https://www.example.com, http://test.org/page, www.google.com
"""

print(f"\nSample text for regex:\n{sample_text[:200]}...")

# Email extraction with validation
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
emails = re.findall(email_pattern, sample_text)
print(f"\nEmails found: {emails}")

# Phone number extraction (multiple formats)
phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phones = re.findall(phone_pattern, sample_text)
print(f"Phone numbers found: {phones}")

# Currency extraction
currency_pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}'
currencies = re.findall(currency_pattern, sample_text)
print(f"Currency amounts found: {currencies}")

# Date extraction (multiple formats)
date_patterns = [
    r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
    r'\d{1,2}/\d{1,2}/\d{4}',  # MM/DD/YYYY
]

all_dates = []
for pattern in date_patterns:
    all_dates.extend(re.findall(pattern, sample_text))

print(f"Dates found: {all_dates}")

# ID extraction
id_pattern = r'ID:\s*([A-Z]{3}\d{3})'
ids = re.findall(id_pattern, sample_text)
print(f"Employee IDs found: {ids}")

# URL extraction
url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?|www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
urls = re.findall(url_pattern, sample_text)
print(f"URLs found: {urls}")

# Advanced: Extract structured data
def extract_employee_data(text):
    """Extract employee information using regex."""
    employee_pattern = r'-\s*([^(-]+)\s*\(([^)]+)\)\s*-\s*Phone:\s*([^(-\d)]*)\s*-\s*ID:\s*([A-Z]{3}\d{3})'

    matches = re.findall(employee_pattern, text)
    employees = []

    for match in matches:
        name, email, phone, emp_id = match
        employees.append({
            'name': name.strip(),
            'email': email.strip(),
            'phone': phone.strip(),
            'employee_id': emp_id.strip()
        })

    return pd.DataFrame(employees)

employee_df = extract_employee_data(sample_text)
print(f"\nExtracted employee data:\n{employee_df}")

# -----------------------------------------------------------------------------
# 7.9 EXCEL AUTOMATION WORKFLOW
# -----------------------------------------------------------------------------
"""
Complete Excel data processing and reporting workflow.
"""

def excel_automation_workflow():
    """Complete Excel processing workflow."""
    # Create sample messy data
    messy_data = {
        'Name': ['Alice Johnson', 'Bob Smith', None, 'Diana Prince', 'Alice Johnson'],
        'Department': ['Engineering', 'Sales', 'Engineering', None, 'Engineering'],
        'Salary': [75000, 65000, 80000, 60000, 75000],
        'Start_Date': ['2020-01-15', '2019-03-20', '2018-11-10', '2021-05-05', '2020-01-15'],
        'Performance_Rating': [4.5, 3.8, None, 4.2, 4.5]
    }

    df = pd.DataFrame(messy_data)
    print(f"\nOriginal messy data:\n{df}")

    # Step 1: Clean column names
    df.columns = df.columns.str.lower().str.replace('_', ' ').str.strip()
    print(f"\nAfter column cleaning:\n{df.columns.tolist()}")

    # Step 2: Handle missing values
    print(f"\nMissing values before cleaning:\n{df.isnull().sum()}")

    # Fill missing names with 'Unknown'
    df['name'] = df['name'].fillna('Unknown')

    # Fill missing departments with mode
    dept_mode = df['department'].mode()[0]
    df['department'] = df['department'].fillna(dept_mode)

    # Fill missing performance ratings with mean
    rating_mean = df['performance rating'].mean()
    df['performance rating'] = df['performance rating'].fillna(rating_mean)

    print(f"\nMissing values after cleaning:\n{df.isnull().sum()}")

    # Step 3: Remove duplicates
    initial_count = len(df)
    df = df.drop_duplicates()
    final_count = len(df)
    print(f"\nRemoved {initial_count - final_count} duplicate rows")

    # Step 4: Data transformations
    df['annual_bonus'] = df['salary'] * 0.1
    df['total_compensation'] = df['salary'] + df['annual_bonus']

    # Convert dates and extract year
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['start_year'] = df['start_date'].dt.year

    print(f"\nAfter transformations:\n{df}")

    # Step 5: Generate summary reports
    dept_summary = df.groupby('department').agg({
        'salary': ['mean', 'min', 'max', 'count'],
        'performance rating': 'mean',
        'total_compensation': 'sum'
    }).round(2)

    print(f"\nDepartment summary:\n{dept_summary}")

    # Step 6: Save to Excel with multiple sheets
    timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
    excel_filename = f'tutorial_employee_report_{timestamp}.xlsx'

    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Cleaned_Data', index=False)
        dept_summary.to_excel(writer, sheet_name='Department_Summary', index=True)

        # Add a summary sheet
        summary_data = {
            'Metric': ['Total Employees', 'Average Salary', 'Total Compensation', 'Departments'],
            'Value': [len(df), df['salary'].mean(), df['total_compensation'].sum(), df['department'].nunique()]
        }
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Report_Summary', index=False)

    print(f"\nExcel report saved as '{excel_filename}'")
    print("Sheets created: Cleaned_Data, Department_Summary, Report_Summary")

    return df, dept_summary

# Run Excel automation
cleaned_data, dept_report = excel_automation_workflow()

# -----------------------------------------------------------------------------
# 7.10 EMAIL AUTOMATION (OPTIONAL)
# -----------------------------------------------------------------------------
"""
Send automated reports via email.
Note: Requires email server configuration and credentials.
"""

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders

# def send_report_email(recipient, subject, body, attachment_path=None):
#     """Send an email with optional attachment."""
#     # Email configuration (use environment variables for security)
#     sender_email = os.environ.get('EMAIL_USER')
#     sender_password = os.environ.get('EMAIL_PASS')
#     smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
#     smtp_port = int(os.environ.get('SMTP_PORT', 587))

#     if not all([sender_email, sender_password]):
#         print("Email credentials not configured")
#         return False

#     try:
#         # Create message
#         msg = MIMEMultipart()
#         msg['From'] = sender_email
#         msg['To'] = recipient
#         msg['Subject'] = subject

#         # Add body
#         msg.attach(MIMEText(body, 'html'))

#         # Add attachment if provided
#         if attachment_path and os.path.exists(attachment_path):
#             with open(attachment_path, 'rb') as attachment:
#                 part = MIMEBase('application', 'octet-stream')
#                 part.set_payload(attachment.read())
#                 encoders.encode_base64(part)
#                 part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
#                 msg.attach(part)

#         # Send email
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.send_message(msg)
#         server.quit()

#         print(f"Email sent successfully to {recipient}")
#         return True

#     except Exception as e:
#         print(f"Failed to send email: {e}")
#         return False

# Example usage (commented out - requires configuration)
"""
report_body = f'''
<h2>Employee Report Summary</h2>
<p>Total employees: {len(cleaned_data)}</p>
<p>Average salary: ${cleaned_data['salary'].mean():,.2f}</p>
<p>Report generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
'''

send_report_email(
    recipient='manager@company.com',
    subject='Weekly Employee Report',
    body=report_body,
    attachment_path='tutorial_employee_report.xlsx'
)
"""

print("\nEmail automation: Requires email server configuration")

# =============================================================================
# TESTING YOUR KNOWLEDGE
# =============================================================================
"""
Practice exercises to reinforce learning.
Uncomment and run individual functions to test.
"""

def test_basic_operations():
    """Test basic Python operations."""
    # Test variables
    name = "Python"
    version = 3.9
    assert name == "Python"
    assert version > 3

    # Test lists
    numbers = [1, 2, 3, 4, 5]
    assert sum(numbers) == 15
    assert len(numbers) == 5

    # Test dictionaries
    person = {"name": "Alice", "age": 25}
    assert person["name"] == "Alice"
    assert person["age"] == 25

    print("✓ Basic operations test passed!")

def test_functions():
    """Test function creation and usage."""
    def calculate_average(nums):
        if not nums:
            return 0
        return sum(nums) / len(nums)

    def find_max(nums):
        if not nums:
            return None
        return max(nums)

    # Test cases
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([]) == 0
    assert find_max([1, 5, 3, 9, 2]) == 9
    assert find_max([]) is None

    print("✓ Functions test passed!")

def test_oop():
    """Test object-oriented programming."""
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    rect = Rectangle(5, 3)
    assert rect.area() == 15
    assert rect.perimeter() == 16

    print("✓ OOP test passed!")

def test_pandas_basics():
    """Test basic Pandas operations."""
    import pandas as pd

    # Create test data
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'score': [85, 92, 78]
    }
    df = pd.DataFrame(data)

    # Test operations
    assert len(df) == 3
    assert df['age'].mean() == 30.0
    assert df['score'].max() == 92

    # Test filtering
    high_scores = df[df['score'] > 80]
    assert len(high_scores) == 2

    print("✓ Pandas basics test passed!")

# Uncomment to run tests
# print("\n" + "="*50)
# print("RUNNING TESTS")
# print("="*50)
# test_basic_operations()
# test_functions()
# test_oop()
# test_pandas_basics()
# print("All tests passed! 🎉")

# =============================================================================
# FINAL PROJECT IDEAS
# =============================================================================
"""
Ideas for capstone projects to apply your learning.
"""

project_ideas = [
    {
        "name": "Personal Finance Tracker",
        "description": "Track income, expenses, and savings with Pandas and Matplotlib",
        "technologies": ["Pandas", "Matplotlib", "CSV/Excel"],
        "features": ["Categorize transactions", "Generate reports", "Visualize spending"]
    },
    {
        "name": "Weather Data Analyzer",
        "description": "Analyze weather patterns from API data",
        "technologies": ["Requests", "Pandas", "Matplotlib"],
        "features": ["Fetch weather data", "Calculate statistics", "Create weather charts"]
    },
    {
        "name": "Book Recommendation System",
        "description": "Scrape book data and build a recommendation engine",
        "technologies": ["BeautifulSoup", "Pandas", "NumPy"],
        "features": ["Web scraping", "Data cleaning", "Similarity matching"]
    },
    {
        "name": "Sales Dashboard",
        "description": "Create an automated sales reporting dashboard",
        "technologies": ["Pandas", "Matplotlib", "SQL"],
        "features": ["Data aggregation", "KPI calculations", "Interactive charts"]
    }
]

print("\n" + "="*60)
print("FINAL PROJECT IDEAS")
print("="*60)

for i, project in enumerate(project_ideas, 1):
    print(f"\n{i}. {project['name']}")
    print(f"   Description: {project['description']}")
    print(f"   Technologies: {', '.join(project['technologies'])}")
    print(f"   Features: {', '.join(project['features'])}")

# =============================================================================
# COURSE SUMMARY
# =============================================================================
"""
What you've accomplished in this comprehensive Python course.
"""

print(f"""
{'='*60}
COURSE COMPLETION SUMMARY
{'='*60}

🎯 SKILLS ACQUIRED:
• Python fundamentals (variables, types, collections)
• Control flow (conditions, loops, exceptions)
• Functions (parameters, returns, lambdas)
• Object-oriented programming (classes, inheritance, encapsulation)
• NumPy arrays and vectorized operations
• Pandas DataFrames and data manipulation
• Matplotlib visualization and plotting
• SQL Server integration
• Web scraping with BeautifulSoup
• Regular expressions for text processing
• Excel automation
• Complete data pipelines

📊 PROJECTS COMPLETED:
• Basic Python programs
• Data analysis scripts
• OOP applications
• Visualization dashboards
• Automated data pipelines

🚀 CAREER APPLICATIONS:
• Data Analyst
• Python Developer
• Data Engineer
• Business Intelligence Analyst
• Automation Specialist

📚 NEXT STEPS:
• Practice with real datasets
• Learn advanced libraries (scikit-learn, TensorFlow)
• Build portfolio projects
• Contribute to open source
• Take advanced Python courses

🎉 Congratulations on completing the Python Data Analysis course!
{'='*60}
""")

# End of tutorial
if __name__ == "__main__":
    print("\nTutorial completed! Check generated files:")
    print("- tutorial_advanced_plots.png")
    print("- tutorial_scraped_quotes.csv")
    print("- tutorial_products.xlsx")
    print("- tutorial_employee_data.csv")
    print("- tutorial_department_summary.xlsx")
    print("- tutorial_compensation_report.txt")
    print("- tutorial_quotes_[timestamp].csv")
    print("- tutorial_employee_report_[timestamp].xlsx")