# 1.Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.
print("="*50)
print("First Problem:")
print("="*50)

print("Enter 5 elements:")
arr = []
for i in range(5):
    element = int(input())
    arr.append(element)
    # region  by using for loop
    # descending = sorted(arr, reverse=True)
    # ascending = sorted(arr)
    # print("Original array:")
    # for element in arr:
    #     print(element)
    # print("Array in descending order:")
    # for element in descending:
    #     print(element)
    # print("Array in ascending order:")
    # for element in ascending:
    #     print(element)
    # endregion

print("Original array:", arr)
print("Array in descending order:", sorted(arr, reverse=True))
print("Array in ascending order:", sorted(arr))

# 2. Generate a multiplication table (n factorial).
print("="*50)
print("Second Problem:")
print("="*50)
n = int(input("Enter a number to generate its multiplication table: "))
print("Multiplication table for", n, ":")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print("="*25)
n = int(input("Enter a number to calculate its factorial: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0 or n == 1:
    print("Factorial of", n, "is 1.")
else:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)

# 3. Simple calculator with arithmetic operations using variables.
print("="*50)
print("Third Problem:")
print("="*50)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")

# 4. Create 3 variables named age, city, and assign values to them, then print them using an f-string.
print("="*50)
print("Fourth Problem:")
print("="*50)

age = 25
city = "Zifta"
print(f"My age is {age} and I live in {city}.")

# 5. Create a list of fruits containing at least five different fruit names, get the first and last items, and reverse the list
print("="*50)
print("Fifth Problem:")
print("="*50)
fruits = ["apple", "banana", "Ananas", "Mango", "Orange"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
fruits.reverse()
print("Reversed list:", fruits)

# 6. Create a list of cities with at least 5 values, use enumerate() to print each city along with its index.
print("="*50)
print("Sixth Problem:")
print("="*50)
cities = ["Zagazig", "Cairo", "Giza", "October", "Tanta"]
for index, city in enumerate(cities):
    print(f"Index: {index}: {city}")

# 7. Create a list of integers from 1 to 20 and use a comprehension to create a new list called squares for these integers.
print("="*50)
print("Seventh Problem:")
print("="*50)
numbers = list(range(1, 21))
squares = [num ** 2 for num in numbers]
print("Squares of integers from 1 to 20:", squares)


