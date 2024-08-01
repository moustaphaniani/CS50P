def main():
    while True:
        # Prompt the user for a 'str' of text
        twttr_input = input("Write the text to Twitter: ")
        try:
            print("Output:",shorten(twttr_input))
            break
        except ValueError:
            exit()

def shorten(word):
    # Logic to output that same text but with all vowels (A, E, I, O, and U) omitted,
    # whether inputted in uppercase or lowercase
    twttr_output = ''
    eliminate = "aAeEiIoOuU"
    #eliminate = "AEIOU"

    for character in word:
        for erase in eliminate:
            if character == erase:
                character = ''
        twttr_output = twttr_output + character
    return twttr_output


if __name__ == "__main__":
    main()
