# Program that:
#
# 1. Prompts the user for a level, n.
#    If the user does not input a positive integer, the program should prompt again.
# 2. Randomly generates an integer between 1 and n, inclusive, using the random module.
# 3. Prompts the user to guess that integer.
#    If the guess is not a positive integer, the program should prompt the user again.
#    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#    If the guess is the same as that integer, the program should output Just right! and exit.

import random

while True:
    try:
        user_level = input("Level: ")
        if user_level.isnumeric() is True:
            number = int(random.randint(1, int(user_level)+1))
            while True:
                try:
                    user_guess = input("Guess: ")
                    if user_guess.isnumeric() is True:
                        if int(user_guess) < number:
                            print("Too small!")
                        elif int(user_guess) > number:
                            print("Too large!")
                        else:
                            print("Just right!")
                            break
                except:
                    break
            break
    except:
        break
