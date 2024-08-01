# Prompt the user for a 'str' of text
twttr_input = input("Write the text to Twitter: ")

# Logic to output that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase
twttr_output = ''
eliminate = "aAeEiIoOuU"

for character in twttr_input:

    for erase in eliminate:

        if character == erase:
            character = ''

    twttr_output = twttr_output + character


print("Output:", twttr_output)
