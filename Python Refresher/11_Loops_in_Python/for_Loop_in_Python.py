friends = ["Rolf", "Bob", "Jen", "Anne"]
# We can create loop to print all friends from the list without constantly repeating print(f"{friends[0]} is my friend!")

for friend in friends:
    print(f"{friend} is my friend!")
# If you have a list with unknown number of values and you want to specify how many times to run the loop !in range()!
for friend in range(3):
    print(f"{friend} is my friend!")

# Using for loop to calculate avarage grade in class
grades = [33, 67, 88, 97, 14, 24, 41]
# Or we can use
# total = sum(grades)
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print("The average grade is : " + str(total/amount))