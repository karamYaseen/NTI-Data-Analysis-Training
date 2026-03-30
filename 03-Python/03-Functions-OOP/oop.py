# Object-Oriented Programming (OOP) in Python - Third Day
# This file covers classes, inheritance, properties, and magic methods

# ===========================================
# WHY OOP MATTERS
# ===========================================
# OOP organizes code around objects that represent real-world entities.
# Benefits:
# - Encapsulation: Hide internal details, expose clean interfaces
# - Inheritance: Reuse code through class hierarchies
# - Polymorphism: Same interface, different implementations
# - Modularity: Objects are self-contained units
# - Maintainability: Changes are localized to classes
#
# Use cases:
# - GUI applications (buttons, windows as objects)
# - Game development (players, enemies, items)
# - Data models (users, products, orders)
# - API clients (connection objects, request objects)
#
# Common pitfalls:
# - Over-inheritance (deep hierarchies become complex)
# - Tight coupling (classes too dependent on each other)
# - God objects (classes that do too many things)
# - Method resolution order confusion in multiple inheritance
# - Forgetting to call super().__init__()

# ===========================================
# BASIC CLASS DEFINITION
# ===========================================

# Creating a simple class
class Person:
    pass

# Creating an instance
t1 = Person()
print(type(t1))  # <class '__main__.Person'>

# Adding attributes dynamically
t1.name = 'sameh'
print(t1.name)  # 'sameh'

# Different instances have separate attributes
t2 = Person()
t2.name = 'mohsen'
print(t2.name, t1.name)  # 'mohsen sameh'

# ===========================================
# METHODS
# ===========================================

# Class with methods
class Dog:
    def bark(self):  # self refers to the instance
        print('haw haw haw')

dog1 = Dog()
dog1.bark()  # Prints: haw haw haw

dog2 = Dog()
dog2.bark()  # Prints: haw haw haw

# Methods can be called on class or instance
Dog.bark(dog1)  # Explicit object passing
dog1.bark()  # Implicit (Python handles self)

# ===========================================
# CONSTRUCTOR (__init__)
# ===========================================

# Constructor without parameters
class Dog:
    def __init__(self):
        self.name = 'rex'
    
    def bark(self):
        print('haw haw haw')

dog1 = Dog()
print(dog1.name)  # 'rex'
dog2 = Dog()
print(dog2.name)  # 'rex'

# Constructor with parameters
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print('haw haw haw')

dog1 = Dog('simba')
print(dog1.name)  # 'simba'

dog2 = Dog('mesh simba')
print(dog2.name)  # 'mesh simba'

# Modifying attributes
dog1.name = 'Joy'
print(dog1.name)  # 'Joy'

# ===========================================
# MULTIPLE ATTRIBUTES AND METHODS
# ===========================================

# Class with multiple attributes and methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("haw haw haw")
    
    def set_age(self, age):
        self.age = age

dog1 = Dog('zeft', 2)
dog1.set_age(3)
print(dog1.age)  # 3

# ===========================================
# PROPERTIES AND VALIDATION
# ===========================================

# Using @property decorator for validation
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("haw haw haw")
    
    def set_age(self, age):
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name.isalpha():
            raise ValueError('Dog name must be letters only')
        self._name = name

dog1 = Dog('juva', 2)
dog1.name = 'mory'  # Valid
print(dog1.name)  # 'mory'

# dog2 = Dog('abc1', 2)  # Raises ValueError

# ===========================================
# STRING REPRESENTATION (__repr__ and __str__)
# ===========================================

# Default representation
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

acct = Account('ahmed', 100)
print(acct)  # <__main__.Account object at 0x...>

# Using __repr__ for better representation
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __repr__(self):
        return f'{self.name} currently has {self.balance} in their account.'

acct = Account('yehia', 900)
print(acct)  # yehia currently has 900 in their account.
print(repr(acct))  # Same output

# ===========================================
# OPERATOR OVERLOADING
# ===========================================

# Overloading the + operator with __add__
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __repr__(self):
        return f'{self.name} currently has {self.balance} in his account'
    
    def __add__(self, other):
        total = self.balance + other.balance
        return f'{self.name} and {other.name} both have a total of {total}'

acct1 = Account('nadeem', 100)
acct2 = Account('yehia', 900)
print(acct1 + acct2)  # nadeem and yehia both have a total of 1000

# ===========================================
# ENCAPSULATION (PRIVATE ATTRIBUTES)
# ===========================================

# Private attributes with name mangling
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.__ssn = '123-45-6789'  # Private attribute

acct = Account('magdy', 300)
# Direct access to private attributes fails
# acct.__ssn  # AttributeError

# But can be accessed with name mangling
acct._Account__ssn = '000000'

# ===========================================
# INHERITANCE
# ===========================================

# Base class
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = fname + '.' + lname + '@email.com'

emp1 = Employee('mohamed', 'tharwat')
print(emp1.email)  # 'mohamed.tharwat@email.com'

# Simple inheritance
class Teacher(Employee):
    pass

tr1 = Teacher('hany', 'hassan')
print(tr1.email)  # 'hany.hassan@email.com'

# Inheritance with method override
class Teacher(Employee):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # Call parent constructor
        self.email = 't-' + fname + '.' + lname + '@email.com'

tr1 = Teacher('ahmed', 'adaweyya')
print(tr1.email)  # 't-ahmed.adaweyya@email.com'

# ===========================================
# MULTIPLE INITIALIZATION AND METHODS
# ===========================================

# Base Employee class
class Employee:
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id

    def work(self) -> str:
        return f'{self.name} is working.'

    def __repr__(self) -> str:
        return f'Employee(Name: {self.name}, ID: {self.employee_id})'

# Doctor class inheriting from Employee
class Doctor(Employee):
    def __init__(self, name: str, employee_id: int, specialty: str):
        super().__init__(name, employee_id)
        self.specialty = specialty

    def diagnose(self) -> str:
        return f'Dr. {self.name}, a {self.specialty}, is diagnosing a patient.'

    def __repr__(self) -> str:
        return (f'Doctor(Name: {self.name}, ID: {self.employee_id}, '
                f'Specialty: {self.specialty})')

# Creating instances
employee1 = Employee("Ahmed hassan", 12345)
print(employee1)  # Employee(Name: Ahmed hassan, ID: 12345)
print(employee1.work())  # Ahmed hassan is working.

doctor = Doctor("Sara ali", 54321, "Cardiology")
print(doctor)  # Doctor(Name: Sara ali, ID: 54321, Specialty: Cardiology)
print(doctor.work())  # Sara ali is working.
print(doctor.diagnose())  # Dr. Sara ali, a Cardiology, is diagnosing a patient.

# ===========================================
# DATA VALIDATION IN METHODS
# ===========================================

# Class with input validation
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('amount must be positive.')

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError('Insufficient funds.')
        else:
            raise ValueError('Amount must be positive.')

acct = Account('ahmed', 230.15)
acct.deposit(50)  # Valid
# acct.deposit(-12)  # Raises ValueError

# ===========================================
# TYPE HINTS AND DOCUMENTATION
# ===========================================

# Function with type hints and docstrings
class Account:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance
        self.__ssn = '123-45-6789'

    def deposit(self, amount: float) -> None:
        """Insert money into the account."""
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Amount must be positive.')

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError('Insufficient funds.')
        else:
            raise ValueError('Amount must be positive.')

    def __repr__(self) -> str:
        return f'{self.name} currently has {self.balance} in their account.'

# ===========================================
# PRACTICAL EXAMPLE: CARD GAME
# ===========================================

# Card class for a simple card game
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [Card(suit, rank) for suit in suits for rank in ranks]
print(f"Total cards in deck: {len(deck)}")  # 52

# Print some cards
for card in deck[:5]:
    print(card)