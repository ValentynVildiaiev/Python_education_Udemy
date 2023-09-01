from colorama import init
from colorama import Fore, Back, Style
# Use Colorama to work on Windows
init()

# Simple Calculator
print(Back.GREEN)
print(Fore.BLACK)
what = input("What should we do (+, -, *, /): ")
print(Fore.CYAN)
print(Back.YELLOW)
a = float(input("Select a first number: "))
b = float(input("Select second number: "))

if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
elif what == "*":
    c = a * b
    print("Result: " + str(c))
elif what == "/":
    c = a / b
    print("Result: " + str(c))
else:
    print("Wrong operation")
input()
