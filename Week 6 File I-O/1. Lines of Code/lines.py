# Program that expects exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .py, or if the specified file does not exist,
# the program should instead exit via sys.exit.

import os
import os.path
import sys


def main():
    #verify argument is passed
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if verify_arguments(sys.argv[1]):
            print(lines_number(sys.argv[1]))


def verify_arguments(arg):
    # Check if file is Python
    if arg.lower().endswith('.py'):
        # Check if file exists
        if os.path.exists(arg):
            return True
        else:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")


def lines_number(file):
    # Open file, read content and close file
    content = open(file, "r")
    full_content = content.read().split("\n")
    content.close()
    # Itinerate througth all lines of code
    for line in range(len(full_content)):
        # Clean spaces before and after each line
        full_content[line] = full_content[line].strip()
        # If lines starts with '#' change to ''
        if full_content[line].startswith("#"):
            full_content[line] = ''
    # Remove all empty lines
    while('' in full_content):
        full_content.remove('')
    # Count how many lines are left
    return int(len(full_content))


if __name__ == "__main__":
    main()
