# 1. Write a function that accepts two arguments (length, start) to
#   generate an array of a specific length filled with integer numbers
#   increased by one from start.
import re
print("="*50)
print("First Problem:")
print("="*50)


def generate_array(length, start):
    return [start + i for i in range(length)]


length = int(input("Enter the length of the array: "))
start = int(input("Enter the starting number: "))
print("Generated array:", generate_array(length, start))

print("="*50)
print("Second Problem:")
print("="*50)

# 2. write a function that takes a number as an argument and if the
#   numberdivisible by 3 return "Fizz" and if it is divisible by 5 return
#   "buzz" and if is is divisible by both return "FizzBuzz"


def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return "Not divisible by 3 or 5 || non FizzBuzz or Fizz or Buzz hhhhhhhhhhh"


number = int(input("Enter a number: "))
print(fizz_buzz(number))

print("="*50)
print("Third Problem:")
print("="*50)

# 3. Write a function which has an input of a string from user then it
#   will return the same string reversed.


def reverse_string(s):
    return s[::-1]


user_input = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(user_input))


# 4. Ask the user for his name then confirm that he has entered his
#   name(not an empty string/integers). then proceed to ask him for
#   his email and print all this data check if it is a valid email
#   or not using regex.
print("="*50)
print("Fourth Problem:")
print("="*50)


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


name = input("Enter your name: ")
if not name.strip() or name.isdigit():
    print("Invalid name. Please enter a valid name.")
    name = input("Enter your name: ")

email = input("Enter your email: ")
if not is_valid_email(email):
    print("Invalid email. Please enter a valid email.")
    email = input("Enter your email: ")
print(f"Name: {name}, Email: {email}")

print("="*50)
print("Fifth Problem:")
print("="*50)

# 5. Write a function that takes a string and prints the
#   longest alphabetical ordered substring occurred For example, if
#   the string is 'abdulrahman' then the output is: Longest substring in
#   alphabetical order is: abdu


def longest_alphabetical_substring(s):
    longest = current = s[0]
    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            current += s[i]
        else:
            current = s[i]
        if len(current) > len(longest):
            longest = current
    return longest


input_string = input("Enter a string: ")
print(
    f"Longest substring in alphabetical order is: {longest_alphabetical_substring(input_string)}")

print("="*50)
print("Sixth Problem:")
print("="*50)

# 6. String Compression
#   Implement a function that compresses a string using the counts of repeated characters.
#   For example, the string "aabcccccaaa" would become "a2b1c5a3".
#   If the compressed string is not shorter than the original, return the original string.


def compress_string(s):
    if len(s) <= 1:
        return s
    compressed = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1
    compressed += s[-1] + str(count)

    return compressed if len(compressed) < len(s) else s


input_string = input("Enter a string to compress: ")
print("Compressed string:", compress_string(input_string))

print("="*50)
print("Seventh Problem:")
print("="*50)

# 7. Rotate Matrix
#   Create a function that rotates a square matrix (2D list) 90 degrees clockwise in place.


def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)
rotated = rotate_matrix(matrix)
print("\nRotated matrix:")
for row in rotated:
    print(row)

print("="*50)
print("Eighth Problem:")
print("="*50)

# Make simple Game card By using class


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

deck = [Card(suit, rank, value) for suit in suits
        for rank in ranks
        for value in values]
print("Deck of cards:")
for card in deck:
    print(f"{card} (Value: {card.value})")
