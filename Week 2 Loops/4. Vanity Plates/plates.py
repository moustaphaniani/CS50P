def main():
    # Prompt the user for a vanity plate
    plate = input("What's your asking Vanity Plate: ")

    # Output 'Valid' if meets all of the requirements or 'Invalid' if it does not
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check that vanity plate contains a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False
    # No periods, spaces, or punctuation marks are allowed.
    elif check_alphanum(s) is False:
        return False
    # check that vanity plate starts with at least two letters
    # check that Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.”
    elif check_digits(s) is False:
        return False
    else:
        return True


def check_alphanum(alnum):
    if alnum.isalnum() is False:
        return False
    else:
        return True


def character_list(string):
    characters_list = []
    for character in string:
        characters_list.append(character)
    return characters_list


def check_digits(start):
    characters = character_list(start)

    if characters[0].isalpha() is False and characters[1].isalpha() is False:
        return False

    actual = 'alpha'
    for i in range(2, len(start)):
        if actual == 'alpha' and characters[i].isalpha() is True:
            actual = 'alpha'
        elif actual == 'alpha' and characters[i].isnumeric() is True and int(characters[i]) != 0:
            actual = 'number'
        elif actual == 'number' and characters[i].isnumeric() is True:
            actual = 'number'
        else:
            return False

    return True


main()
