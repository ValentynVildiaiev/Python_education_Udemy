# Destructuring variables
# Brackets are nor necessary, they are only necessary when Python might be confused when you want to create a tuple
# or these are values in another collection

# x = [(5, 11)] # List with the tuple inside it


# This one x = 5, 11 can be decomposed into the two variables x , y = 5, 11
tupl = 5, 11  # Tuple also can be decomposed
x, y = tupl
print(x, y)

#
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100, "Paul": 97}
print(list(student_attendance.items())) # This one returned to a list because .items() doesn't quite return a list of
# tuples, but it returns something very similar. The differences are small


people = [("Bob", 43, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age ,profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


print("Same with using indexes without destructuring a variable")
#  Same with using indexes without destructuring a variable
for persons in people:
    print(f"Name: {persons[0]}, Age: {persons[1]}, Profession: {persons[2]}")

# In Python variables can contain and even start with an underscore,
# and that is frequently used as a variable when you want to ignore one
print("In Python variables can contain and even start with an underscore,"
      "and that is frequently used as a variable when you want to ignore one")

person = ("Bobby", 41, "Mechanic")
# this will create three variables name, _, profession where name = "Bobby", _ = 41, profession = "Mechanic"
# So if you use _ that means that you don't care about this variable and its meant to be ignored
name, _, profession = person
print(name, profession)

# If we want to separate 5 elements into two lists
# teh *tail IS a Syntax for collecting, all values that will be destructed
# and not assigned to other variables will be stored in *tail

# so the first value will become a head, and everything else will be collected into the *tail
head, *tail = [1, 2, 3, 4, 5]
print(head)
# You don't need to use * again to use tail variable
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(head)
# You don't need to use * again to use head variable
print(tail)