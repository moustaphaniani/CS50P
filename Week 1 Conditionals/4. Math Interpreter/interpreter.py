# Prompt the user for an arithmetic expression
expression = input("Write your arithmetic expression: ")

# Logic of the program
'''
Calculates and outputs the result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
x is an integer
y is +, -, *, or /
z is an integer
'''

result = round(float(eval(expression)), 1)
print(result)
