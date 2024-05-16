#name = input("Enter your name: ")
#age = int(input("What is you age?:  "))
#print("Hello " + name + " your age is: " + str(age))
#mood = input("How are you today?: ")
#print("So your mood is: " + mood + " Glad to hear that")
#name = input()
#print(name.swapcase())

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)
