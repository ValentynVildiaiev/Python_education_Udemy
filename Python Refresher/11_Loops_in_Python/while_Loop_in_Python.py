number = 7
# Capital Y and lower case n is default convention in programming,where Y will always be default:


# WHILE makes indented code running over again form the END back to user_input != "n" : while user_input != "n":
# While True: Will create an infinite loop
# If using while True: Wee need to add TERMINATE option!!!!! within the loop code
while True:
    user_input = input("Would you like to play? (Y/n) ")
    if user_input == 'n':
        break


    user_number = int(input("Guess out the number: "))
    if user_number == number:
        print("Congratz you guess correctly")
    # This one is bit better than use in keyword to convert values -1 and 1 for example user input is 8 or 6
    elif abs(number - user_number) == 1:
        print("You were off by one")
    elif user_number >= 20:
        print("You're number is way off bigger than magic number ")
    else:
        print("Sorry wrong number")


