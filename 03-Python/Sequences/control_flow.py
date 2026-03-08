# Control Flow in Python - Second Day
# This file covers conditional statements (if/elif/else) and loops (while/for)

# ===========================================
# CONDITIONAL STATEMENTS
# ===========================================

# Basic if statement
car = 'bmw'
if car == 'bmw':
    print('Yes it is')

# if with boolean True
car = 'bmw'
if True:
    print('Yes it is')

# Truthiness - nonzero values are true
if 1:
    print('Nonzero values are true, so this will print')

if 0:
    print('Zero is false, so this will not print')

# String standardization in conditional tests
# Consider standardizing string when used in conditional tests (i.e case, stripping, etc.)

# Multiple conditions with and/or
age = int(input('How old are you?'))
if 60 >= age >= 45:
    print("You are still young!!")

# if...else
age = int(input('How old are you?'))
if 60 >= age >= 45:
    print("You are still young!!")
else:
    print("Sorry!")

# if...elif..else chain
age = int(input('How old are you?'))
if 60 >= float(age) >= 45:
    print("You are still young!!")
elif age < 45:
    print("Too young ya man!")
else:
    print("A bit old")

# Multiple tests example
grade = 80
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

# Nested if statements
age = int(input('How old are you?'))
country = input('Enta mneen ?')
if 60 >= float(age) >= 45:
    if country.lower() == 'egypt':
        print("You are an Egyptian")
    else:
        print("enta 3adi")
else:
    print("mashi")

# Conditional Expressions (ternary operator)
grade = int(input("enter your grade"))
if grade >= 60:
    result = 'Passed'
else:
    result = 'Failed'
print(result)

# Shorter version
result = 'Passed' if grade >= 60 else 'Failed'
print(result)

# With different data types
'even' if int(input('Enter an integer:')) % 2 == 0 else 'odd'
[2,4,6] if int(input('Enter an integer:')) % 2 == 0 else [1,3,5]

# Nested conditional expressions
grade = 50
'A' if grade >= 90 else ('B' if grade >= 80 else ('C' if grade >= 70 else ('D' if grade >= 60 else 'F')))

# List comprehensions with conditionals
l = [i * 10 if i % 2 == 0 else i for i in range(1,15)]
print(l)

# pass statement - placeholder for future code
if True:
    pass

# ===========================================
# LOOPS
# ===========================================

# while loop
counter = 1
while counter < 90:
    counter *= 3
print(counter)

# while with printing
counter = 1
while counter < 90:
    print(f'[{counter}', end=' ')
    counter *= 3
    print(f'{counter}]', end=' ')
print()

# while with list manipulation
my_list = ['foul', 'flafel', 'batates', 'pickles', 'koshary', 'betengan']
while len(my_list) > 0:
    print(my_list[-1])
    my_list.pop()
    print(my_list)
    print('--')
print('---\nalf hana ya brens:)')

# while with break
retries = 1
while retries <= 3:
    user_input = input('type a number: ')
    if not user_input.isdigit():
        retries += 1
    else:
        print(f'Finally! the square root of the number you entered is {(int(user_input)**(1/2)):.4f}')
        break

if retries > 2:
    print('rabbena yehdeek')

# for loop - iterating through sequences
foods = ['foul', 'falafel', 'batates', 'pickles', 'koshary', 'betengan']
for food in foods:
    print(food)

# for with strings
some_text = 'This is a string'
for letter in some_text:
    print(f'{letter}')

# for with different data types
foods_set = {'foul', 'falafel', 'batates', 'pickles', 'koshary', 'betengan'}
foods_tuple = ('foul', 'flafel', 'batates', 'pickles', 'koshary', 'betengan')
foods_dictionary = {
    '1': 'foul',
    '2': 'falafel',
    '3': 'batates',
    '4': 'pickles',
    '5': 'koshary',
    '6': 'betengan'
}

for food in foods_set:
    print(food)
print('-----')

# enumerate for index and value
for index, food in enumerate(foods_tuple):
    print(index, food)

# Dictionary iteration
for food in enumerate(foods_dictionary.values()):
    print(food[1])

for food in foods_dictionary.items():
    print(food)

for counter, (index, food) in enumerate(foods_dictionary.items()):
    print(index, food)

for index, item in list(enumerate(foods_dictionary.values())):
    print(index, item)

# break in for loop
foods = ['foul', 'falafel', 'batates', 'pickles', 'koshary', 'betengan']
for food in foods:
    if food == 'pickles':
        print('tamam keda :)')
        break
    print(food)

# nested for with if - prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, 'is a prime number')

# continue statement
for counter in range(1,22):
    if counter % 2 == 0:
        print(f'{counter} is even')
    else:
        print(f'{counter} is odd')

# continue alternative
for counter in range(1,22):
    if counter % 2 == 0:
        print(f'{counter} is even')
        continue
    print(f'{counter} is odd')

# continue with strings
for letter in "This is a simple string":
    if letter == 'i':
        continue
    print(letter)

# else with for
for num in range(20):
    if num % 3 == 0:
        print(f'{num} is dividable by 3')
else:
    print(num)