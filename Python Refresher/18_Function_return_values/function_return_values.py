# None - is a special value in Python that means no value,missing value,undeclared value
# Functions return None by default
# That means whenever you call a function you can assign it's return value to a variable

def add(x, y):
    return x + y  # The run result will be nothing because we didn't print anything,but function is working


add(5, 8)
result = add(5, 8)  # To get printed result without None you need to provide a variable with the result of a function
print(result)


# You can do two returns in one function until only one of them is running
# Most commonly it used with an "if"  statement
# So 'return' depends only on one condition
# Usually not recommended to have function returning multiple different TYPES of data
# This function can return number and a string just because we want to perform mathematics on the return of function
def divide(dividend, divisor):
    if divisor != 0:
        return dividend/divisor
    else:
        return "You can't divide by zero"


result_div = divide(15, 3)
print(result_div)
