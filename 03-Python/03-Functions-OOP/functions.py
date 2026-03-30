# Functions in Python - Third Day
# This file covers function definition, parameters, return values, and advanced function concepts

# ===========================================
# WHY FUNCTIONS MATTER
# ===========================================
# Functions are reusable blocks of code that perform specific tasks.
# Benefits:
# - Code reusability: Write once, use many times
# - Modularity: Break complex problems into smaller, manageable pieces
# - Maintainability: Changes in one place affect everywhere it's used
# - Readability: Give meaningful names to code blocks
# - Testing: Test individual functions separately
#
# Use cases:
# - Data processing pipelines
# - Mathematical calculations
# - API interactions
# - File operations
#
# Common pitfalls:
# - Mutable default arguments (use None + check)
# - Side effects (functions should return values, not modify globals)
# - Deep recursion (can cause stack overflow)
# - Over-complication (keep functions focused on single responsibility)

# ===========================================
# FUNCTION BASICS
# ===========================================

# Function definition and calling
def greeting():
    name = input('What is your name?')
    print(f'Welcome to Python {name}')

# Function call
greeting()

# ===========================================
# PARAMETERS AND ARGUMENTS
# ===========================================

# Single parameter
def greeting(username):
    print(f'Welcome to Python Mr. {username.title()}!')

greeting('ahmed')

# Multiple parameters
def pets(owner_name, pet_name):
    print(f'Hi {owner_name.title()} please take care of {pet_name.title()}!')

pets('ahmed', 'Memo')
pets('memo', 'ahMed')

# Keyword arguments
pets(pet_name='memo', owner_name='ahmed')

# ===========================================
# DEFAULT VALUES
# ===========================================

# Default parameter values
def pets(owner_name, pet_name='nemo'):
    print(f'Hi {owner_name.title()} please take care of {pet_name.title()}!')

pets('ahmed')  # pet_name uses default value
pets('ahmed', 'Fluffy')  # pet_name is overridden

# Multiple default parameters
def fullname(fname='x', mname='y', lname='z'):
    return f'Your full name is: {fname.title()} {mname.title()} {lname.title()}'

fullname('sami', 'sara', 'salim')
fullname('sami')
fullname(lname='Ahmed')

# Optional arguments (default must be last)
def fullname(fname, lname, mname=''):
    if mname:
        return f'Your full name is: {fname.title()} {mname.title()} {lname.title()}'
    else:
        return f'Your full name is: {fname.title()} {lname.title()}'

fullname('sami', 'sara', 'salim')
fullname('sami', 'sara')

# ===========================================
# RETURN VALUES
# ===========================================

# Basic return
def pets(owner_name='ahmed', pet_name='nemo'):
    advice = f'Hi {owner_name.title()} please take care of {pet_name.title()}!'
    return advice

result = pets()
print(result)
print(type(result))

# Multiple return values
def get_info():
    return 'Ahmed', 25, 'Engineer'

name, age, job = get_info()

# ===========================================
# DOCSTRINGS
# ===========================================

# Using docstrings to document functions
def fullname(fname, lname, mname=''):
    """
    Returns a full name for a given triplet of firstname, middlename, and last name.
    
    Parameters:
        fname: First name (required)
        lname: Last name (required)
        mname: Middle name (optional)
    
    Returns:
        str: Formatted full name
    """
    if mname:
        return f'Your full name is: {fname.title()} {mname.title()} {lname.title()}'
    else:
        return f'Your full name is: {fname.title()} {lname.title()}'

# Access docstring
# help(fullname)
# fullname?
# fullname??

# ===========================================
# ARBITRARY ARGUMENTS (*args)
# ===========================================

# Variable number of arguments
def average(*args):
    """Calculate average of any number of arguments."""
    return sum(args) / len(args)

average(1, 2, 3, 4, 5)
average(10, 20)

# ===========================================
# SCOPE: LOCAL VS GLOBAL
# ===========================================

# Global variable
x = 10

# Function accessing global variable
def access_global():
    print('x printed from access_global:', x)

access_global()  # Prints 10

# Local variables shadow global variables
def try_to_modify_global():
    x = 3.5
    print('x printed from try_to_modify_global:', x)

try_to_modify_global()  # Prints 3.5
print(x)  # Still prints 10 (global x unchanged)

# Using global keyword to modify global variable
def modify_global():
    global x
    x = 'hello'
    print('x printed from modify_global:', x)

modify_global()  # Prints 'hello'
print(x)  # Now prints 'hello' (global x modified)

# ===========================================
# PARAMETER PASSING: VALUE VS REFERENCE
# ===========================================

# Immutable objects (numbers, strings, tuples)
x = 13

def cube(number):
    print('id(number):', id(number))
    return number ** 3

print('id(x):', id(x))
cube(x)  # Same id before modification
cube(13)  # Same id

# Modifying immutable creates new object
def cube_modify(number):
    print('id(number) before:', id(number))
    number **= 3
    print('id(number) after:', id(number))
    return number

cube_modify(x)  # Different id after modification

# ===========================================
# HIGHER-ORDER FUNCTIONS
# ===========================================

# Function as argument: map()
def cuber(x):
    return x ** 3

my_list = [2, 3, 4]
result = map(cuber, my_list)
print(list(result))  # [8, 27, 64]

# Using map with built-in functions
numbers = ['1', '2', '3', '4']
int_numbers = list(map(int, numbers))

# filter() function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# ===========================================
# LAMBDA EXPRESSIONS (ANONYMOUS FUNCTIONS)
# ===========================================

# Lambda syntax: lambda arguments: expression

# Simple lambda
square = lambda x: x ** 2
square(5)  # Returns 25

# Lambda with multiple arguments
add = lambda x, y: x + y
add(3, 4)  # Returns 7

# Complex lambda expression
f = lambda x, y: 3 * (x ** 2) + 2 * y - 5
f(2, 3)  # Returns 15

# Lambda with map()
my_list = [2, 3, 4]
result = list(map(lambda x: x ** 3, my_list))
# [8, 27, 64]

# Lambda with sort key
names = ['machael jackson', 'ahmed helmy', 'magdi shatta']
names.sort(key=len)  # Sort by length

names.sort(key=lambda name: name.split(' ')[-1])  # Sort by last name

# ===========================================
# NESTED FUNCTIONS AND CLOSURES
# ===========================================

# Function returning function
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))  # 22
print(mytripler(11))  # 33

# ===========================================
# PRACTICAL EXAMPLES
# ===========================================

# Generate array with specific length and start
def generate_array(length, start):
    return [start + i for i in range(length)]

length = 5
start = 10
print(generate_array(length, start))  # [10, 11, 12, 13, 14]

# FizzBuzz function
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

for i in range(1, 16):
    print(fizz_buzz(i))

# String reversal
def reverse_string(s):
    return s[::-1]

print(reverse_string('hello'))  # 'olleh'