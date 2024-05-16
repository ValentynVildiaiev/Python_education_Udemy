number = 7
user_input = input("Enter 'y' if you want to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess out the number: "))
    if user_number == number:
        print("Congratz you guess correctly")
    # Or you can use ABSOLUTE abs(number - user_number) == 1: to convert values -1 and 1 to 1
    # This one is bit better than use in keyword
    elif number - user_number in (1, -1):
        print("You were off by one")
    elif user_number >= 20:
        print("You're number is way off bigger than magic number ")
    else:
        print("Sorry wrong number")
else:
    print("Sorry you need to select 'y' to play the game!")
