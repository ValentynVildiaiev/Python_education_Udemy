# Dictionaries another structure in Python like lists,sets and tuples that allow us to interact with data in certain way
# Dictionaries used for associate keys and values together if you know the key you can get a value easily
# "Rolf" - key; 24 - value

friend_ages = {"Rolf": 24, "Bob": 32, "Alex": 35, "Adam": 30}

# To change a particular element or add one
friend_ages["Paul"] = 36
friend_ages["Adam"] = 27
print(friend_ages["Alex"])
print(friend_ages)

# Creating a dictionary with more data
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 25},
    {"name": "Anne", "age": 27}
]
print(friends)

# Access to the name and age from the dictionary
print(friends[1]["name"], str(friends[1]["age"]))
print("Iterating over a dictionary")
# Iterating over a dictionary
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}%")
print("Better way to interact is:")

# Better way to interact is:
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")
print("Using in keyword to check whether a value is one of the keys")

# Using in keyword to check whether a value is one of the keys
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")

print("Getting only values back without worrying about the keys")

# "Getting only values back without worrying about the keys"
attendance_values = student_attendance.values()
print(attendance_values / len(attendance_values)) # Expected sum divided for length of dictionary which is 3 in our case

# ""

