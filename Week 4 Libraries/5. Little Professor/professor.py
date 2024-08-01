# Program that:
#
# 1. Prompts the user for a level, n.
#    If the user does not input 1, 2, or 3, the program should prompt again.
# 2. Randomly generates ten (10) math problems formatted as X + Y = ,
#    wherein each of X and Y is a non-negative integer with n digits.
#    No need to support operations other than addition (+).
# 3. Prompts the user to solve each of those problems.
#    If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
#    allowing the user up to three tries in total for that problem.
#    If the user has still not answered correctly after three tries, the program should output the correct answer.
# 4. The program should ultimately output the user’s score: the number of correct answers out of 10.

import random

def main():
    operations = 0

    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 1
        while tries <= 3:
            user_answer = input(f"{x} + {y} = ")
            if user_answer.isnumeric() is True and int(user_answer) == x + y:
                operations += 1
                break
            else:
                print("EEE")
            tries += 1

        if tries == 4:
            print(f"{x} + {y} = {x + y}")

        continue
    print(f"Score: {operations}")

def get_level():
    while True:
        try:
            user_level = input("Level: ")
            if user_level.isnumeric() is True and 1 <= int(user_level) <= 3:
                return int(user_level)
        except:
            break


def generate_integer(level):
    minimum_numbers = [0, 10, 100]
    minimum = minimum_numbers[int(level) - 1]
    maximum = '9' * int(level)
    return random.randint(int(minimum), int(maximum))


if __name__ == "__main__":
    main()
