day_of_week = input("What day of the week is it today?: ").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's Tuesday.")
else:
    print("The week is on full speed ahead")

# Out of the if statement and unrelated
print("This always run")

num = int(input("Enter number: "))
# ==, !=, <, >, <=, >=
if num >= 55:
    print("You guess correctly")
    if num == 100:
        print("Num is 100")
elif num == 40:
    print("Num is 40")
else:
    print("Ty again your number is wrong ")

# Simple selection
a = int(input("First number: "))
b = int(input("Second number: "))

if a > b:
    c = "a is bigger than b"
    print(c)
elif a == b:
    d = "a is equal to b"
    print(d)
elif a < b:
    e = "a is smaller than b"
    print(e)
else:
    print("Make an input")

# Boolean selection
isHappy = True
if not isHappy:
    print("Yay you are happy")
else:
    print("Happy indeed")


