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

# Output Variables
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Output Variables
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
