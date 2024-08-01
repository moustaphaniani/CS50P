# Logic of the program:
#
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

import sys

def main():
 while True:
    # Prompt the user for a greeting
    greeting = input("What's your greeting? ")
    try:
        # Return output from logic of the program
        print(f"${value(greeting)}")
        break
    except ValueError:
        sys.exit()

def value(user_input):
    if user_input.strip().lower().startswith("hello"):
        return 100
    elif user_input.strip().lower().startswith("h"):
        return 20
    else:
        return 0


if __name__ == "__main__":
    main()
