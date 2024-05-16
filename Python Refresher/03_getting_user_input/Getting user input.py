name = input('Enter your name: ')

#DOING MATH WITH USER INPUT

size_input = input("How big is your house (in square meters): ")   # User input is always a string value that needs to be converted
square_metres = int(size_input)
square_feats = square_metres * 10.8
print(f"{square_metres} square meters is equal to {square_feats:.2f} square feat") # :.2f Will shorten the output to 2 numbers after the DOT.