# How to give functions data so they can use it

# pass means DO NOTHING
# Functions expect at least something inside them,because Python expects intended block inside
# Params x and y, when the Python runs function itself this two variables are created x and y,and function can use them
# inside the function body, when you get to the end of the function body those variables are DISAPPEAR
def add(x, y):
    #  pass
    result = x + y
    print(result)


add(5, 3)  # Numbers inside called ARGUMENTS


# Function without any parameters

def say_hello():
    print("Hello!")


# If you use the function WITHOUT params and try to pass it with adding an ARGUMENT
# say_hello("Bob") # TypeError: say_hello() takes 0 positional arguments but 1 was given

# Use the PARAM to pass the ARGUMENT
def say_hello_name(name):
    print(f"Hello, {name}")


say_hello_name("Bob")


# Positional Arguments means that Arguments equal to number of params

def say_hello_name_sur(name, surname):
    print(f"Hello, {name} {surname}")


say_hello_name_sur("Bob", "Smith")

# KEYWORD OR NAMED ARGUMENTS!
# EXAMPLE
# They are really helpfully because they allow us to easily determine when we're reading line which argument responsible
# for which parameter

say_hello_name_sur(surname="Bob", name="Smith")


# DO NOT separate argument from its param with space surname="Bob", divisor=9 and etc.
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You can't divide by zero")


# POSITIONAL ARGUMENTS FOLLOWS THE KEYWORD AFRGUMENT

divide(6, divisor=4)  # you can combine positional arguments with keyword arguments
