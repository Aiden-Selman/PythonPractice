# A simple print statement
print("Hello, World!")

# python indentation is very important. In other languages its for readability, in python its crucitial to execution
# python uses indentation to indicate a block of code
if 5 > 2:
  print("Five is greater than two!")

# this will work
if 5 > 2:
print("Five is greater than two!")

# this gives a syntax error

# how to declare variables in python
x = 5
y = "Hello, World!"

# casting variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# how to get the type of a variable 
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or double quotes to declare
# String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

# Variables are case-sensitive
a = 4
A = "Sally"
# A will not overwrite a

# Assigning multiple variables at home
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
