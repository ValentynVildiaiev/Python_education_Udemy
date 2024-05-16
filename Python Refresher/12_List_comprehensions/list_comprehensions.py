numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers] # we can add num * 2 and for cycle to shorten the description
# The one way of doubling the numbers from one list to another
for num in numbers:
    doubled.append(num * 2)

# Creating a new list that contain names with S
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")] # Other shorter way to do it without loop
# Cycle to select only names that starts with "S" with for if statement
for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)

cities = ["Seattle", "Sacramento", "Boston", "Houston", "Vinnytsia", "Sumy"]
city_s = [city for city in cities if city.startswith("S")]

print(city_s)
