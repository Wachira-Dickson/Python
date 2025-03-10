Python

Introduction

Python is a high-level, interpreted programming language known for its simplicity and readability. 
It supports multiple programming paradigms, including procedural, object-oriented, 
and functional programming. This document provides an overview of Python's core functionalities.

Basic Syntax

Python uses indentation to define code blocks, which makes it highly readable. Here’s a simple example of a Python script:

print("Hello, World!")

Variables and Data Types

Python supports various data types, including:

Integers (int): Whole numbers, e.g., 10

Floating-point numbers (float): Decimal numbers, e.g., 10.5

Strings (str): Text data, e.g., 'Hello'

Booleans (bool): True or False


Python uses control Flow statements, such as:

Conditional Statements

Python uses if, elif, and else for conditional logic:

x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

Loops

Python supports for and while loops:

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

Functions

Functions are defined using the def keyword:

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))


Object-Oriented Programming (OOP)

Python supports classes and objects:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 25)
print(person1.introduce())

Modules and Packages

Python allows code reuse through modules and packages:

# Importing a module
import math
print(math.sqrt(16))


Python's simplicity, versatility, and vast ecosystem of libraries make it suitable for various applications,
including web development, data science, machine learning, automation, and more.
