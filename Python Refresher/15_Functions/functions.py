def hello():
    print("Hello")


# Calling running or executing a function are all synonyms, so when you create a function you create a callable variable
# Creating or defining a function DOES NOT run the function body.
# It just tells Python that variable hello exists
# To run a single standing function you need to type -> hello()

hello()

print("Welcome to the age in seconds program!")


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"your age in seconds is : {age_seconds} ! ")


user_age_in_seconds()

print("Good Bye !")


# Things you SHOULD NOT DO working with functions is REUSE names

def print():
    print("Hello World!")


print()

# Calling a print function now will throw an error TypeError: print() takes 0 positional arguments but 1 was given


# Need to AVOID reusing friends variable in two different places
# Because even though you are using a variable friends, you are also defining a new variable called friends
# You CAN'T use variable in the same line where you defining  a variable
# its also looks like x = x + 5 BUT x doesn't exist
# Never use shadow variable name from an outer scope!

# def add_friend():
# friend_name = input("Enter your friend name: ")
# friends = friends + [friend_name]


# You CAN'T use the functions before they get defined!

say_hello()


def say_hello():
    print("Hello!")


# This may look like an error because in the line 60 friends variable has not been defined yet
# But actually this line runs only when line 65 runs so this is OK
# If you will run the function multiple times friends will become ['Rolf', 'Rolf', 'Rolf']
def add_friend():
    friends.append("Rolf")


friends = []
add_friend()
print(friends)
