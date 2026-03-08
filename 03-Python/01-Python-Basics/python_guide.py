# Python Fundamentals - Complete Guide
# A comprehensive explanation of Python basics and sequences

"""
╔══════════════════════════════════════════════════════════════╗
║                    PYTHON FUNDAMENTALS GUIDE                 ║
║                    Understanding the Basics                  ║
╚══════════════════════════════════════════════════════════════╝

This guide explains all the fundamental concepts covered in your Python training.
Each section includes explanations, examples, and key points to remember.
"""

# ==========================================
# SECTION 1: PYTHON BASICS
# ==========================================

"""
1. DATA TYPES IN PYTHON
Python has several built-in data types that store different kinds of information.
"""

# ===== NUMBERS =====
"""
Numbers in Python come in two main types:
- Integers (int): Whole numbers like 5, -12, 1000
- Floats (float): Decimal numbers like 3.14, -0.5, 2.0

Key Points:
- No size limit for integers (can be very large)
- Use underscores for readability: 1_000_000 instead of 1000000
- Floats have decimal precision limitations
"""

# Examples:
age = 25                    # Integer
height = 5.9               # Float
big_number = 1_000_000     # Readable large number

# ===== STRINGS =====
"""
Strings are sequences of characters enclosed in quotes.
They represent text data in Python.

Key Points:
- Can use single quotes: 'Hello'
- Can use double quotes: "Hello"
- Can use triple quotes for multi-line: '''Hello World'''
- Strings are immutable (cannot be changed after creation)
"""

# Examples:
name = "Alice"                    # Double quotes
greeting = 'Hello World'          # Single quotes
message = '''This is a
multi-line string'''              # Triple quotes

# ===== VARIABLES =====
"""
Variables are names that store data values.
Think of them as labeled containers for your data.

Key Points:
- Variable names should be descriptive
- Cannot start with numbers
- Case-sensitive (age ≠ Age)
- Use snake_case for multi-word names
"""

# Examples:
user_name = "John"      # Good: descriptive, snake_case
age = 30               # Good: clear meaning
x = 5                  # Bad: not descriptive

# ===== BASIC OPERATIONS =====
"""
Python supports all standard mathematical operations.
"""

# Arithmetic Operations:
x = 10
y = 3

print(x + y)    # Addition: 13
print(x - y)    # Subtraction: 7
print(x * y)    # Multiplication: 30
print(x / y)    # Division: 3.333...
print(x // y)   # Floor Division: 3 (removes decimal)
print(x % y)    # Modulus (remainder): 1
print(x ** y)   # Power: 1000

# ===== USER INPUT =====
"""
Getting input from users allows interactive programs.

Key Point:
- input() ALWAYS returns a string, even for numbers!
- Must convert to numbers if needed
"""

# Examples:
# name = input("What's your name? ")        # Returns string
# age = int(input("How old are you? "))     # Convert to integer

# ===== TYPE CONVERSION =====
"""
Converting between data types when needed.
"""

# Examples:
number_str = "123"
number_int = int(number_str)      # "123" → 123

float_num = 3.14
int_num = int(float_num)          # 3.14 → 3 (loses decimal)

age = 25
age_str = str(age)                # 25 → "25"

# ===== BOOLEAN VALUES =====
"""
Booleans represent True or False.
Used for decision making and logic.
"""

# Examples:
is_student = True
has_graduated = False

# Comparison operators create booleans:
print(5 > 3)      # True
print(10 == 5)    # False
print(7 != 3)     # True

# ===== OBJECT-ORIENTED CONCEPTS =====
"""
Everything in Python is an object with methods and attributes.
"""

# Examples:
name = "python"
print(name.upper())      # 'PYTHON'
print(name.title())      # 'Python'
print(len(name))         # 6

number = 42
print(number.bit_length())  # Number of bits needed

# ==========================================
# SECTION 2: SEQUENCES
# ==========================================

"""
2. SEQUENCES IN PYTHON
Sequences are ordered collections of items.
Python has several types of sequences.
"""

# ===== LISTS =====
"""
Lists are mutable (changeable) sequences.
They can store different types of data.

Key Points:
- Created with square brackets: [1, 2, 3]
- Can mix data types: [1, "hello", True]
- Zero-indexed (first item is at index 0)
- Mutable: can add, remove, change items
"""

# Creating lists:
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", True, 3.14]

# Accessing items:
print(fruits[0])     # "apple" (first item)
print(fruits[-1])    # "orange" (last item)
print(fruits[1:3])   # ["banana", "orange"] (slicing)

# ===== LIST METHODS =====
"""
Common operations on lists:
"""

fruits = ["apple", "banana"]

# Adding items:
fruits.append("orange")           # Add to end
print(fruits)                     # ["apple", "banana", "orange"]

fruits.insert(1, "grape")         # Insert at position
print(fruits)                     # ["apple", "grape", "banana", "orange"]

# Removing items:
fruits.remove("banana")           # Remove by value
print(fruits)                     # ["apple", "grape", "orange"]

last_fruit = fruits.pop()         # Remove and return last item
print(last_fruit)                 # "orange"
print(fruits)                     # ["apple", "grape"]

# ===== LIST SORTING =====
"""
Organizing list data:
"""

numbers = [3, 1, 4, 1, 5]
numbers.sort()                    # Sort in place
print(numbers)                    # [1, 1, 3, 4, 5]

numbers.sort(reverse=True)        # Sort descending
print(numbers)                    # [5, 4, 3, 1, 1]

# Sort without changing original:
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)                   # [3, 1, 4, 1, 5] (unchanged)
print(sorted_list)                # [1, 1, 3, 4, 5]

# ===== LIST COMPREHENSIONS =====
"""
Concise way to create lists from other sequences.
"""

# Traditional way:
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension:
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With conditions:
even_squares = [x ** 2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)  # [4, 16]

# ===== TUPLES =====
"""
Tuples are immutable (unchangeable) sequences.
Similar to lists but cannot be modified after creation.

Key Points:
- Created with parentheses: (1, 2, 3)
- Cannot add, remove, or change items
- Faster than lists for read-only data
- Can be used as dictionary keys
"""

# Creating tuples:
point = (3, 4)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma!

# Accessing items (same as lists):
print(point[0])      # 3
print(colors[-1])    # "blue"

# Tuples are immutable:
# colors[0] = "yellow"  # This would cause an error!

# ===== STRINGS AS SEQUENCES =====
"""
Strings are sequences of characters.
Many sequence operations work on strings.
"""

text = "Hello World"

# Accessing characters:
print(text[0])       # "H"
print(text[-1])      # "d"
print(text[1:5])     # "ello"

# String methods:
print(text.upper())      # "HELLO WORLD"
print(text.lower())      # "hello world"
print(text.title())      # "Hello World"
print(text.split())      # ["Hello", "World"]
print(text.replace("World", "Python"))  # "Hello Python"

# ===== ENUMERATE FUNCTION =====
"""
Gets both index and value when iterating.
Very useful for numbered lists.
"""

fruits = ["apple", "banana", "orange"]

# Without enumerate:
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate:
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# ==========================================
# SECTION 3: PRACTICAL EXAMPLES
# ==========================================

"""
3. COMMON PATTERNS AND EXAMPLES
Real-world usage examples.
"""

# ===== BUILDING LISTS DYNAMICALLY =====
# Start with empty list and add items
scores = []
# scores.append(int(input("Enter score: ")))  # Would get user input

# ===== FINDING ITEMS =====
fruits = ["apple", "banana", "orange", "grape"]

if "banana" in fruits:
    print("Banana is in the list!")

# Get index of item:
banana_index = fruits.index("banana")
print(f"Banana is at position {banana_index}")

# ===== COUNTING OCCURRENCES =====
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # How many 2's? Answer: 3

# ===== COPYING LISTS =====
original = [1, 2, 3]

# Wrong way (both variables point to same list):
copy1 = original
copy1.append(4)
print(original)  # [1, 2, 3, 4] - original changed!

# Right way:
copy2 = original.copy()  # or original[:]
copy2.append(5)
print(original)  # [1, 2, 3, 4] - original unchanged
print(copy2)     # [1, 2, 3, 4, 5]

# ===== WORKING WITH STRINGS =====
# Common string operations
user_input = "  hello world  "
clean_input = user_input.strip()  # Remove spaces
capitalized = clean_input.title() # Capitalize words
print(capitalized)  # "Hello World"

# Check string properties:
email = "user@example.com"
print(email.endswith(".com"))     # True
print(email.startswith("admin"))  # False
print("@" in email)               # True

# ===== TYPE CHECKING =====
"""
Checking data types before operations.
"""

def process_data(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, (int, float)):
        return data * 2
    elif isinstance(data, list):
        return len(data)
    else:
        return "Unknown type"

print(process_data("hello"))    # "HELLO"
print(process_data(5))          # 10
print(process_data([1,2,3]))    # 3

# ==========================================
# SECTION 4: COMMON ERRORS TO AVOID
# ==========================================

"""
4. FREQUENT MISTAKES AND HOW TO FIX THEM
"""

# ===== INDEX ERRORS =====
fruits = ["apple", "banana"]
# print(fruits[2])  # IndexError! Only indices 0, 1 exist

# Safe access:
if len(fruits) > 1:
    print(fruits[1])

# ===== TYPE ERRORS =====
# age = input("Enter age: ")  # This is a string!
# birth_year = 2024 - age     # TypeError!

# Fix:
# age = int(input("Enter age: "))
# birth_year = 2024 - age

# ===== MUTABILITY CONFUSION =====
# Strings are immutable:
name = "John"
# name[0] = "j"  # TypeError!

# Fix:
name = "j" + name[1:]  # "john"

# ===== LIST MODIFICATION DURING ITERATION =====
# Don't modify a list while iterating over it:
numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # This can cause problems!

# Better approach:
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]  # Keep only odd numbers

# ==========================================
# SECTION 5: BEST PRACTICES
# ==========================================

"""
5. WRITING GOOD PYTHON CODE
Tips for clean, readable code.
"""

# ===== DESCRIPTIVE NAMES =====
# Good:
user_age = 25
total_price = 99.99
customer_list = []

# Bad:
x = 25
tp = 99.99
cl = []

# ===== CONSISTENT FORMATTING =====
# Use consistent indentation (4 spaces)
# Add spaces around operators
# Use blank lines to separate logical sections

def calculate_total(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    return total

# ===== COMMENTS AND DOCSTRINGS =====
def greet_user(name):
    """
    Greet a user by name.

    Args:
        name (str): The user's name

    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"

# ===== ERROR HANDLING =====
def divide_numbers(a, b):
    """Divide two numbers safely."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Please provide numbers only!"

# ===== USE BUILT-IN FUNCTIONS =====
# Instead of writing your own functions, use Python's built-ins:
numbers = [3, 1, 4, 1, 5]

# Good:
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
count = len(numbers)

# ==========================================
# SUMMARY
# ==========================================

"""
KEY TAKEAWAYS:

1. DATA TYPES:
   - Numbers (int, float), Strings, Booleans
   - Everything is an object with methods

2. VARIABLES:
   - Store data with descriptive names
   - Case-sensitive, snake_case preferred

3. SEQUENCES:
   - Lists: mutable, versatile
   - Tuples: immutable, faster
   - Strings: character sequences

4. OPERATIONS:
   - Arithmetic: +, -, *, /, //, %, **
   - Comparisons: ==, !=, <, >, <=, >=
   - Logic: and, or, not

5. BEST PRACTICES:
   - Write readable code
   - Handle errors gracefully
   - Use appropriate data structures
   - Comment your code

Remember: Practice makes perfect! Try writing small programs
using these concepts to reinforce your learning.
"""

# ===== QUICK REFERENCE =====
"""
USEFUL FUNCTIONS AND METHODS:

# Built-in functions:
len()           # Length of sequence
max(), min()    # Maximum/minimum values
sum()           # Sum of numbers
sorted()        # Sort without changing original
enumerate()     # Get index and value
range()         # Generate number sequences

# String methods:
.upper()        # Convert to uppercase
.lower()        # Convert to lowercase
.title()        # Capitalize each word
.strip()        # Remove whitespace
.split()        # Split into list
.replace()      # Replace text

# List methods:
.append()       # Add to end
.insert()       # Add at position
.remove()       # Remove by value
.pop()          # Remove and return
.sort()         # Sort in place
.copy()         # Create copy
"""