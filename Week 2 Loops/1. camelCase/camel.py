# Prompt the user for the name of a variable in camel case
camel_case = input("Write the name of a variable in camel case: ")

# Logic to output the corresponding name in snake case
output = ''
for character in camel_case:

    if character == character.upper():
        character = "_"  + character.lower()

    output = output + character


print(output)
