# Python Basics
# This file covers fundamental Python concepts including data types, variables, and basic operations

# ===== NUMBERS =====
# Integers
12
12 + 32

# Floats
12.8

# Large numbers with underscores for readability
universe_age = 14_000_000_000
print(universe_age)

# ===== VARIABLES AND ASSIGNMENT =====
# Variable assignment
x = 3
y = 7
total = x + y
print(total)

# Multiple assignments
x, y, z = 1, 2, 3

# Same value to multiple variables
x = y = 108

# ===== AUGMENTED ASSIGNMENT =====
x = 10
x += 10  # x = x + 10
print(x)

x -= 10  # x = x - 10
print(x)

x *= 10  # x = x * 10
print(x)

x **= 10
print(x)

# ===== MATHEMATICAL OPERATIONS =====
print(2 ** 10)  # Power
print(9 ** (1 / 2))  # Square root

# True Division (/) vs. Floor Division (//)
print(7 / 4)   # 1.75
print(7 // 4)  # 1 (floor division)

# Remainder Operator
print(7.5 % 3.5)

# Grouping with parentheses
print(10 * (5 + 3))  # 80
print(10 * 5 + 3)    # 53

# ===== STRINGS =====
# Different ways to define strings
"This is a string"
'This is also a string'

# Escaping quotes
"The language 'Python' is named after Monty Python, not the snake."
'I told my friend, \'Python is my favorite language!\' '

# Multiline strings
"""This is a multiline
string that spans
multiple lines"""

# ===== STRING OPERATIONS =====
# Built-in print function
print('Welcome to Python!')
print("\tPython")  # Tab
print("Languages:\nPython\nC\nJavaScript")  # Newline
print("Languages:\n\tPython\n\tC\n\tJavaScript")  # Tab and newline

# String concatenation
age = 45
print('I am', age, 'years old')

# Built-in math functions
print(abs(-45))
print(chr(69))
print(ord('M'))
print(len('python'))
print(max(45, 12, -90, 56, 1))
print(min(45, 12, -90, 56, 1))
print(sum([45, 12, -90, 56, 1]))

# ===== USER INPUT =====
# Getting input from user (always returns string)
# name = input("What's your name? ")
# print('Hello Miss. ' + name)

# Converting input to numbers
# value1 = input('Enter first number: ')
# value2 = input('Enter second number: ')
# value1 + value2  # This concatenates strings!

# Proper way with type conversion
# name = input('What is your name? ')
# yob = int(input('And what is your year of birth?'))
# age = 2025 - yob
# print ('Hi', name, ',you are ', age, 'years old')

# ===== DATA TYPES =====
# Everything is an object - checking types
print(type(7))
print(type(12.2))
print(type('python'))
print(type("""python"""))
print(type('''python'''))

# Dynamic typing
x = 3
print(type(x))
x = "hello"
print(type(x))

# ===== OBJECT METHODS =====
# Strings as objects
name = "  Python Basics  "
print(name.title())
print(name.upper())
print(name.strip())

# Numbers as objects
x = 109
print(x.bit_length())
print(bin(x))
print(float(x))

z = 1.7e3
print(z)
print(int(z).bit_length())

# Using dir() to see available methods
age = 45
# dir(age)  # Shows all available methods

# ===== BOOLEAN VALUES =====
print(True)
print(False)
print(type(not 89 < 100))

# Comparison operators
print(1 == 2)
print(12 != 18)

# Truthiness
print(bool(9892.3))  # Non-zero numbers are True
print(bool(-209))
print(bool(0))       # Zero is False

print(bool("Hello")) # Non-empty strings are True
print(bool(" "))     # Space is True
print(bool(""))      # Empty string is False

# Converting to/from boolean
print(str(False))
print(int(True))     # True = 1, False = 0
print(5 + True)      # 6
print(13 * False)    # 0

# ===== NONE TYPE =====
print(type(None))
print(None is None)
print(None == False)  # False
print(bool(None))     # False
print(bool(None) == bool(""))  # Both False

# ===== IDENTITY AND MEMBERSHIP =====
# 'in' operator
print('e' in 'Hello')
print('3' in [1, 2, 3])
print(3 in [1, 2, 3])

# 'is' operator (identity)
print('Hello' is 'Hello')  # Same string literals
print(10 is 10)           # Small integers

# Identity vs equality
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True (same values)
print(x is y)  # False (different objects)

# But for small integers:
x = 14
y = 14
print(x is y)  # True (Python optimizes small integers)

# ===== ZEN OF PYTHON =====
import this