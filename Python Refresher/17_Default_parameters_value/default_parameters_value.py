# You can pass the arguments to function
def add(x, y=8):  # This means that x is a REQUIRED parameter and y is an OPTIONAL parameter
    print(x + y)


add(5)  # If you doesn't pass a parameter to y it will use default parameter

default_y = 3


def addin(x, y=default_y):
    sum = x + y
    print(sum)


addin(2)
# If you wil change the value to 4 it will return the same value back from the function
# Changing variable that has been used as a default parameter value DOES NOT MODIFY the function
default_y = 4
addin(2)
