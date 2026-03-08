# Exception Handling in Python - Second Day
# This file covers error handling, try/except blocks, and debugging techniques

# ===========================================
# BASIC EXCEPTION HANDLING
# ===========================================

# Handling the ZeroDivisionError Exception
try:
    5 / 0
except:
    print('something wrong happened')

# Getting exception information
try:
    5 / 0
except Exception as e:
    print(e)

# Specific exception handling
try:
    5 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")

# Multiple except blocks
try:
    print(aa)  # NameError
except ZeroDivisionError:
    print("You cannot divide by zero")
except Exception as err:
    print(f'something wrong happened which is {err}')

# else clause - executes if no exceptions
try:
    # 5 / 0  # Uncomment to test exception
    print("z")  # This will work
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print('something wrong happened')
else:
    print('no errors found')

# finally clause - always executes
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# Raising exceptions
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Silent failure
try:
    5 / 0
except:
    pass
print('as if nothing happened')

# ===========================================
# COMMON EXCEPTION TYPES
# ===========================================

# ValueError - invalid value
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError - operation on incompatible types
try:
    "string" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# IndexError - list index out of range
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError - dictionary key not found
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"KeyError: {e}")

# FileNotFoundError - file doesn't exist
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# ===========================================
# ADVANCED EXCEPTION HANDLING
# ===========================================

# Multiple exception types in one except
try:
    # Try different errors by uncommenting
    # result = 5 / 0
    # result = int("abc")
    result = [1, 2, 3][10]
except (ZeroDivisionError, ValueError, IndexError) as e:
    print(f"Caught multiple possible errors: {e}")

# Exception hierarchy
try:
    5 / 0
except Exception as e:  # Catches all exceptions
    print(f"General exception: {e}")
except ZeroDivisionError as e:  # This won't be reached
    print(f"Specific ZeroDivisionError: {e}")

# Custom exception messages
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers!")
        return None

print(divide_numbers(10, 2))  # Should work
print(divide_numbers(10, 0))  # ZeroDivisionError
print(divide_numbers(10, "a"))  # TypeError

# ===========================================
# PRACTICAL EXAMPLES
# ===========================================

# Safe user input
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

# Test the function
# number = get_number("Enter a number: ")
# print(f"You entered: {number}")

# File handling with proper cleanup
def read_file_safely(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'!")
        return None
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return None

# Dictionary access with error handling
def safe_dict_access(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Key '{key}' not found in dictionary!")
        return default

# Test
test_dict = {"name": "John", "age": 30}
print(safe_dict_access(test_dict, "name"))  # Should work
print(safe_dict_access(test_dict, "address"))  # KeyError handled

# List access with bounds checking
def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        print(f"Index {index} is out of range for list of length {len(lst)}!")
        return None

# Test
test_list = [1, 2, 3, 4, 5]
print(safe_list_access(test_list, 2))  # Should work
print(safe_list_access(test_list, 10))  # IndexError handled