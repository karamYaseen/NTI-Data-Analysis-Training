# Python Sequences
# This file covers ordered sequences: Lists, Tuples, and Strings

# ===== LISTS =====
# Creating lists
numbers = [54, -12, 0, 77, 1976]
print(numbers)
print(type(numbers))

# Mixed data types in lists
misc = [(1, 2), 'Ahmed', 47, [25, -9]]
print(misc)

# Multi-line list definition
bicycles = ['trek',
            'cannondale',
            'redline',
            'specialized']
print(bicycles)

# ===== ACCESSING LIST ELEMENTS =====
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])           # Second element
print(bicycles[1].title())   # With string method
print(bicycles[-1])          # Last element
print(bicycles[-2])          # Second to last

# Using individual values
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# ===== MODIFYING LISTS =====
# Changing elements (lists are mutable)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# Building list dynamically
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Concatenating lists
num1 = [12, 423, 109]
num2 = [99, -24]
num = num1 + num2
print(num)

# Repeating lists
num = [2, 4, 7]
print(num * 2)

# ===== REMOVING ELEMENTS =====
# Using del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# Using pop() method (removes and returns)
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()  # Removes last element
print(motorcycles)
print(popped_motorcycle)

# Pop from specific position
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Remove by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

# ===== ORGANIZING LISTS =====
# Sorting permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Sorting temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original:", cars)
print("Sorted:", sorted(cars))
print("Original again:", cars)

# Reversing list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# List length
print(len(cars))

# ===== LIST CONSTRUCTOR =====
print(list([1, 3, 4, 5]))
print(list('Python'))

# ===== ENUMERATE FUNCTION =====
# Manual indexing
values = ['first', 'second', 'third', 'fourth']
for index in range(len(values)):
    value = values[index]
    print(index, value)

# Using enumerate
print(list(enumerate(values)))  # As list of tuples

for index, value in enumerate(values):
    print(index, value)

# ===== AVOIDING INDEX ERRORS =====
# This would cause IndexError:
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[5])  # Out of range

# Empty list error:
# motorcycles = []
# print(motorcycles[-1])  # IndexError

# ===== MAKING NUMERICAL LISTS =====
# Using range()
print(list(range(5)))
print(list(range(20, 2, -2)))  # With step

# Range in loops
for value in range(1, 5):
    print(value)

# Creating number lists
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# ===== LIST COMPREHENSIONS =====
# Manual way
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# List comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# ===== STATISTICS WITH LISTS =====
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Min:", min(digits))
print("Max:", max(digits))
print("Sum:", sum(digits))

# ===== SLICING LISTS =====
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])    # First 3
print(players[2:])     # From index 2 to end
print(players[:4])     # Up to index 4
print(players[0:5:2])  # Every other element

# Looping through slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# ===== COPYING LISTS =====
# Proper way to copy
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Creates a copy

my_foods.append('ice cream')
print("My foods:", my_foods)
print("Friend's foods:", friend_foods)

# Wrong way (both variables point to same list)
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # Same reference

my_foods.append('ice cream')
print("My foods:", my_foods)
print("Friend's foods:", friend_foods)  # Also changed!

# Alternative copy method
my_drinks = ['shai', 'bebsy', '3er2soos']
friend_drinks = my_drinks.copy()
my_drinks.append('sa7lab')
print("My drinks:", my_drinks)
print("Friend's drinks:", friend_drinks)

# ===== TUPLES =====
# Defining tuples (immutable)
dimensions = (200, 50, 100)
print(dimensions[0])
print(dimensions[1])
print(dimensions[2])

# Tuples with different types
two_d = ((0, 19), (23, -4), (91, 54.2))
print(two_d)

misc_d = (15, 'abc', (9, 1), [1, 2, 3], {'def': 15})
print(misc_d)

# Looping through tuples
dimensions = (200, 50, 92)
for dimension in dimensions:
    print(dimension)

# Tuple methods
print(dimensions.count(200))
print(dimensions.index(92))

# Enumerate with tuples
values = ('first', 'second', 'third', 'fourth')
for index, value in enumerate(values):
    print(index, value)

# "Modifying" tuples (actually creating new tuple)
dimensions = (200, 50, 88)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)  # New tuple
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# ===== STRINGS AS SEQUENCES =====
# Strings are immutable sequences
string = 'Hello Everyone'
print(string[0])      # Access characters
print(string.count('e'))

# String methods (many sequence operations)
print(dir(string))    # Shows available methods

# Converting string to list
print(list(string))