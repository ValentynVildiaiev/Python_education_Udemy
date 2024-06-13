# Lambda function is type of function which doesn't have a name and only use return values
# Lambda function exclusively used to operate on inputs and return outputs
# Lambda functions used to return outputs
lambda x, y: x + y
# Lambda functions should be used in the same line where it was defined
# To use lambda function:
(lambda x, y: x + y)(7, 9)
# To get something visible lambda function should be surrounded to print()
print((lambda x, y: x + y)(7, 9))

# Also Lambda function can be assigned for a variable
add = lambda x, y: x + y
print(add(5, 8))


# Lambda are ment to be SHORT functions often used WITHOUT name

# Usefully lambda functions:
def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled = [double(x) for x in sequence]
print(doubled)
# Less confusing is using of map() function
doubled_map = map(double, sequence)
print(doubled_map)

# Same example with lambda function: A bit unreadable
doubled_lam = [(lambda x: x * 2)(x) for x in sequence]
print(doubled_lam)
# Other way with map
doubled_lam_map = list([map(lambda x: x * 2, sequence)])
print(doubled_lam_map)
