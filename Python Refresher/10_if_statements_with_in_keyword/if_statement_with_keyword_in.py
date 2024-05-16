movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter the movie you've watched recently: ")
# using in keyword in the if statement
if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print(f"I haven't watched {user_movie} yet!")

