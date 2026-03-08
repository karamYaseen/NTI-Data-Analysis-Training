# Python Unordered Sequences - Sets & Dictionaries
# A comprehensive guide to Sets and Dictionaries in Python

"""
╔══════════════════════════════════════════════════════════════╗
║                PYTHON UNORDERED SEQUENCES                   ║
║                 Sets & Dictionaries Guide                    ║
╚══════════════════════════════════════════════════════════════╝

This guide covers unordered data structures in Python.
Unlike lists and tuples, these don't maintain element order.
"""

# ==========================================
# SECTION 1: SETS
# ==========================================

"""
SETS - UNIQUE, UNORDERED COLLECTIONS

Sets are collections of unique elements with no duplicates.
They are unordered, meaning elements have no specific position.
"""

# ===== CREATING SETS =====
"""
Sets can be created using curly braces {} or the set() function.
"""

# Creating sets with curly braces:
set1 = {1, 3, 4, 4, 6, 8, 9, 9}
print(set1)  # {1, 3, 4, 6, 8, 9} - duplicates removed automatically

# Creating empty set (can't use {} as that's for empty dict):
empty_set = set()
print(type(empty_set))  # <class 'set'>

# Creating sets from other iterables:
my_list = ['one', 'one', 'two', 'three', 'three', 'four']
my_set = set(my_list)
print(my_set)  # {'one', 'two', 'three', 'four'} - duplicates removed

# Converting back to list:
list_again = list(set(my_list))
print(list_again)  # ['one', 'two', 'three', 'four']

# ===== SET METHODS =====
"""
Common set operations and methods.
"""

# Initialize a set:
my_set = {1, 3}
print(my_set)

# Adding elements:
my_set.add(15)
my_set.add(100)
my_set.add(100)  # Adding duplicate - no effect
print(my_set)     # {1, 3, 15, 100}

# Adding multiple elements:
my_set.update([4, 5], {1, 6, 8})  # Can add lists and other sets
print(my_set)     # {1, 3, 4, 5, 6, 8, 15, 100}

# Removing elements:
my_set.discard(4)  # Safe removal - no error if element not found
print(my_set)

my_set.remove(15)  # Will raise KeyError if element not found
print(my_set)

# Clear all elements:
# my_set.clear()
# print(my_set)  # set()

# ===== SET OPERATIONS =====
"""
Mathematical set operations: union, intersection, difference, symmetric difference.
"""

# Initialize two sets:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# UNION - All elements from both sets (no duplicates):
print("Union:")
print(A | B)           # Using | operator
print(A.union(B))      # Using method
print(B.union(A))      # Same result

# INTERSECTION - Elements common to both sets:
print("\nIntersection:")
print(A & B)                 # Using & operator
print(A.intersection(B))    # Using method

# DIFFERENCE - Elements in A but not in B:
print("\nDifference A - B:")
print(A - B)                 # Using - operator
print(A.difference(B))      # Using method

print("\nDifference B - A:")
print(B - A)                 # Using - operator
print(B.difference(A))      # Using method

# SYMMETRIC DIFFERENCE - Elements in either set but not both:
print("\nSymmetric Difference:")
print(A ^ B)                           # Using ^ operator
print(A.symmetric_difference(B))      # Using method

# ===== SET MEMBERSHIP & ITERATION =====
"""
Testing membership and iterating through sets.
"""

# Membership testing:
print(2 in A)      # True
print(2 in B)      # False
print(6 not in A)  # True

# Iterating through sets:
for num in A:
    print(num)     # Order is not guaranteed!

# ===== SET COMPREHENSIONS =====
"""
Creating sets using comprehension syntax.
"""

# Set comprehension:
squares = {x ** 2 for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}

# With conditions:
even_squares = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {4, 16, 36, 64, 100}

# ===== FROZEN SETS =====
"""
Immutable sets - cannot be modified after creation.
"""

# Creating frozen sets:
frozen = frozenset([1, 2, 3, 4, 5])
print(frozen)
print(type(frozen))

# Frozen sets are immutable:
# frozen.add(6)  # AttributeError!
# frozen.remove(1)  # AttributeError!

# But they support all read operations:
print(3 in frozen)
print(len(frozen))
print(frozen & {3, 4, 5, 6})  # Intersection works

# ===== SET USE CASES =====
"""
When to use sets:

1. Removing duplicates from a list:
   unique_items = list(set(original_list))

2. Membership testing (very fast):
   if item in my_set:  # O(1) average time complexity

3. Finding common elements:
   common = set1 & set2

4. Finding unique elements:
   unique_in_first = set1 - set2

5. Mathematical set operations:
   - Union: all elements from both
   - Intersection: common elements
   - Difference: elements only in first set
   - Symmetric difference: elements in either but not both
"""

# ==========================================
# SECTION 2: DICTIONARIES
# ==========================================

"""
DICTIONARIES - KEY-VALUE PAIR COLLECTIONS

Dictionaries store data as key-value pairs.
Keys must be immutable (strings, numbers, tuples).
Values can be any data type.
"""

# ===== CREATING DICTIONARIES =====
"""
Dictionaries use curly braces {} with key:value pairs.
"""

# Creating dictionaries:
human1 = {'height': 180, 'weight': 80, 'eye-color': 'green', 'language': 'mongolian'}
print(human1)
print(type(human1))

# Empty dictionary:
empty_dict = {}
print(type(empty_dict))

# Using dict() constructor:
human2 = dict(height=160, weight=52, eye_color='brown', language='british')
print(human2)

# ===== ACCESSING DICTIONARY ELEMENTS =====
"""
Access values using keys in square brackets [].
"""

# Accessing values:
print(human1['height'])      # 180
print(human1['language'])    # 'mongolian'

# Using get() method (safer - returns None if key doesn't exist):
print(human1.get('weight'))      # 80
print(human1.get('age'))         # None
print(human1.get('age', 25))     # 25 (default value)

# ===== DICTIONARY METHODS =====
"""
Common dictionary operations.
"""

# Get all keys:
print(human1.keys())    # dict_keys(['height', 'weight', 'eye-color', 'language'])

# Get all values:
print(human1.values())  # dict_values([180, 80, 'green', 'mongolian'])

# Get all key-value pairs:
print(human1.items())   # dict_items([('height', 180), ('weight', 80), ...])

# Length of dictionary:
print(len(human1))      # 4

# ===== MODIFYING DICTIONARIES =====
"""
Adding, updating, and removing elements.
"""

# Adding new key-value pairs:
human1['gender'] = 'male'
print(human1)

# Updating existing values:
human1['weight'] = 82
print(human1)

# Updating multiple values:
human1.update({'height': 182, 'language': 'english'})
print(human1)

# Removing elements:
del human1['gender']  # Remove specific key
print(human1)

# Remove and return value:
eye_color = human1.pop('eye-color')
print(eye_color)      # 'green'
print(human1)

# Clear entire dictionary:
# human1.clear()
# print(human1)  # {}

# ===== DICTIONARY ITERATION =====
"""
Iterating through dictionaries.
"""

# Iterate through keys:
for key in human1:
    print(f"{key}: {human1[key]}")

# Iterate through keys explicitly:
for key in human1.keys():
    print(key)

# Iterate through values:
for value in human1.values():
    print(value)

# Iterate through key-value pairs:
for key, value in human1.items():
    print(f"{key} -> {value}")

# ===== NESTED DICTIONARIES =====
"""
Dictionaries can contain other dictionaries.
"""

# Nested dictionary:
humans = {
    1: {'name': 'John', 'age': 27, 'gender': 'Male'},
    2: {'name': 'Marie', 'age': 22, 'gender': 'Female'},
    3: {'name': 'Shawkat', 'age': 62, 'gender': 'Male'}
}

print(humans)

# Accessing nested values:
print(humans[1]['age'])      # 27
print(humans[2]['name'])     # 'Marie'

# Modifying nested values:
humans[3]['name'] = 'Rabso'
humans[3]['age'] = 100
humans[3]['gender'] = 'Male'
print(humans[3])

# Adding new nested entry:
humans[4] = {'name': 'Gamal', 'age': 47, 'married': 'No'}
print(humans[4])

# ===== DICTIONARIES WITH COMPLEX VALUES =====
"""
Dictionary values can be lists, sets, or other dictionaries.
"""

# Dictionary with list values:
human3 = {
    'name': 'Ahmed',
    'age': 45,
    'languages': ['Arabic', 'English']
}
print(human3['languages'][1])  # 'English'

# Dictionary with mixed key types:
human4 = {
    'name': 'Ahmed',
    'age': 45,
    'languages': ['Arabic', 'English'],
    19: 19  # Number as key
}
print(human4[19])  # 19

# ===== DICTIONARY COMPREHENSIONS =====
"""
Creating dictionaries using comprehension syntax.
"""

# Dictionary comprehension:
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With conditions:
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Converting two lists to dictionary:
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Cairo']
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Cairo'}

# ===== DICTIONARY USE CASES =====
"""
When to use dictionaries:

1. Storing related data with meaningful keys:
   person = {'name': 'John', 'age': 30, 'city': 'NYC'}

2. Fast lookups by key:
   phone_book = {'Alice': '555-1234', 'Bob': '555-5678'}
   print(phone_book['Alice'])  # Very fast lookup

3. Counting occurrences:
   word_count = {}
   for word in text.split():
       word_count[word] = word_count.get(word, 0) + 1

4. Grouping data:
   students_by_grade = {}
   for student in students:
       grade = student['grade']
       if grade not in students_by_grade:
           students_by_grade[grade] = []
       students_by_grade[grade].append(student)

5. Configuration settings:
   config = {
       'database': {'host': 'localhost', 'port': 5432},
       'api': {'timeout': 30, 'retries': 3}
   }
"""

# ==========================================
# SECTION 3: PRACTICAL EXAMPLES
# ==========================================

"""
REAL-WORLD EXAMPLES USING SETS AND DICTIONARIES
"""

# ===== EXAMPLE 1: REMOVING DUPLICATES =====
# Using sets to remove duplicates while preserving order:
def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

original = [1, 2, 2, 3, 4, 4, 5, 1]
unique = remove_duplicates_preserve_order(original)
print(unique)  # [1, 2, 3, 4, 5]

# ===== EXAMPLE 2: WORD COUNT =====
# Using dictionary to count word frequencies:
def count_words(text):
    word_count = {}
    words = text.lower().split()

    for word in words:
        # Remove punctuation
        word = word.strip('.,!?')
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

text = "Hello world! Hello Python. Python is great."
counts = count_words(text)
print(counts)  # {'hello': 2, 'world': 1, 'python': 2, 'is': 1, 'great': 1}

# ===== EXAMPLE 3: STUDENT GRADE ANALYSIS =====
# Using dictionaries for student data analysis:
students = {
    'Alice': {'math': 85, 'science': 92, 'english': 88},
    'Bob': {'math': 78, 'science': 85, 'english': 90},
    'Charlie': {'math': 92, 'science': 88, 'english': 85}
}

# Calculate average grades:
def calculate_averages(students):
    averages = {}
    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        averages[student] = round(avg, 2)
    return averages

student_averages = calculate_averages(students)
print(student_averages)  # {'Alice': 88.33, 'Bob': 84.33, 'Charlie': 88.33}

# Find students who scored above 85 in all subjects:
def find_excellent_students(students):
    excellent = []
    for student, grades in students.items():
        if all(score >= 85 for score in grades.values()):
            excellent.append(student)
    return excellent

excellent_students = find_excellent_students(students)
print(excellent_students)  # ['Alice', 'Charlie']

# ===== EXAMPLE 4: INVENTORY MANAGEMENT =====
# Using sets for inventory operations:
store_a = {'apple', 'banana', 'orange', 'grape'}
store_b = {'banana', 'orange', 'pear', 'kiwi'}

# Products available in both stores:
common_products = store_a & store_b
print(f"Common products: {common_products}")

# Products unique to store A:
unique_to_a = store_a - store_b
print(f"Unique to A: {unique_to_a}")

# All products across both stores:
all_products = store_a | store_b
print(f"All products: {all_products}")

# ===== EXAMPLE 5: PHONE BOOK =====
# Dictionary-based phone book:
phone_book = {
    'Alice': {'home': '555-1234', 'work': '555-5678'},
    'Bob': {'mobile': '555-9012'},
    'Charlie': {'home': '555-3456', 'work': '555-7890', 'mobile': '555-1111'}
}

# Find all phone numbers for a person:
def get_all_numbers(phone_book, name):
    if name in phone_book:
        return phone_book[name]
    return {}

alice_numbers = get_all_numbers(phone_book, 'Alice')
print(alice_numbers)  # {'home': '555-1234', 'work': '555-5678'}

# Search for person by number:
def find_by_number(phone_book, number):
    for name, numbers in phone_book.items():
        if number in numbers.values():
            return name
    return None

owner = find_by_number(phone_book, '555-3456')
print(owner)  # Charlie

# ==========================================
# SECTION 4: COMMON PATTERNS & BEST PRACTICES
# ==========================================

"""
BEST PRACTICES FOR SETS AND DICTIONARIES
"""

# ===== SET PATTERNS =====

# 1. Fast membership testing:
allowed_users = {'alice', 'bob', 'charlie'}
if username in allowed_users:
    print("Access granted")

# 2. Removing duplicates from list:
unique_items = list(set(original_list))

# 3. Finding differences:
old_users = {'alice', 'bob', 'charlie'}
new_users = {'bob', 'charlie', 'david'}
added_users = new_users - old_users      # {'david'}
removed_users = old_users - new_users    # {'alice'}

# 4. Set operations for data analysis:
survey_a = {'python', 'java', 'c++'}
survey_b = {'python', 'javascript', 'c++'}
both_like = survey_a & survey_b           # {'python', 'c++'}
only_a_likes = survey_a - survey_b        # {'java'}
only_b_likes = survey_b - survey_a        # {'javascript'}

# ===== DICTIONARY PATTERNS =====

# 1. Safe dictionary access:
# Bad:
# if 'key' in my_dict:
#     value = my_dict['key']
# else:
#     value = default

# Good:
value = my_dict.get('key', default)

# 2. Dictionary merging (Python 3.9+):
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}

# 3. Counting with defaultdict:
from collections import defaultdict
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1

# 4. Grouping data:
groups = defaultdict(list)
for item in data:
    key = item['category']
    groups[key].append(item)

# ===== PERFORMANCE CONSIDERATIONS =====

# Sets vs Lists for membership:
# - Sets: O(1) average lookup time
# - Lists: O(n) lookup time

# Dictionary operations:
# - Access by key: O(1) average
# - Search by value: O(n) - requires iteration

# Memory usage:
# - Sets/Dicts use more memory than lists for small collections
# - But provide faster operations for large datasets

# ===== COMMON MISTAKES =====

# 1. Modifying dictionary during iteration:
# Wrong:
# for key in my_dict:
#     if some_condition:
#         del my_dict[key]  # RuntimeError!

# Right:
# keys_to_delete = [key for key in my_dict if some_condition]
# for key in keys_to_delete:
#     del my_dict[key]

# 2. Using mutable objects as dictionary keys:
# Wrong:
# my_dict = {[1, 2]: 'value'}  # TypeError!

# Right:
# my_dict = {(1, 2): 'value'}  # Tuples are immutable

# 3. Confusing set operations:
# Wrong:
# result = set1 + set2  # TypeError!

# Right:
# result = set1 | set2  # Union

# ==========================================
# SUMMARY
# ==========================================

"""
KEY TAKEAWAYS:

SETS:
- Unique, unordered collections
- Fast membership testing
- Mathematical set operations (union, intersection, difference)
- Mutable (can add/remove elements)
- Cannot contain mutable objects (lists, dicts)

DICTIONARIES:
- Key-value pair collections
- Keys must be immutable (strings, numbers, tuples)
- Values can be any type
- Fast lookups by key
- Support nesting and complex data structures

WHEN TO USE:
- Sets: When you need unique items or set operations
- Dictionaries: When you need to associate data with meaningful keys
- Both: When order doesn't matter and you need fast operations

BOTH ARE FUNDAMENTAL TO PYTHON PROGRAMMING!
"""

# ===== QUICK REFERENCE =====

# SETS:
"""
Creation: {1, 2, 3} or set([1, 2, 3])
Add: add(item) or update(iterable)
Remove: remove(item) or discard(item)
Operations: | (union), & (intersection), - (difference), ^ (symmetric diff)
Membership: item in my_set
"""

# DICTIONARIES:
"""
Creation: {'key': 'value'} or dict(key='value')
Access: dict['key'] or dict.get('key', default)
Modify: dict['key'] = value
Methods: keys(), values(), items()
Delete: del dict['key'] or dict.pop('key')
"""