# Program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
# and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
# Format the table using the library’s grid format.
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv,
# or if the specified file does not exist, the program should instead exit via sys.exit.

from tabulate import tabulate
import os
import os.path
import sys

def main():
    # Verify if al least 1 argument is passed
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # Verify if more than 1 argument is passed
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Only chance to have is 1 aargument passed
    else:
        if verify_arguments(sys.argv[1]):
            table = pizza_table(sys.argv[1])
            print(tabulate(table, headers="firstrow", tablefmt="grid"))


def pizza_table(file):
    # Open file, read content and close file
    full_content = open(file, "r")
    content = full_content.read().split("\n")
    full_content.close()
    # Retrieve headers as 1st line of data
    for line in range(len(content)):
        content[line] = content[line].split(',')
    content.pop()
    # Retrieve table as the other lines of data
    #table = content.split(',')
    return content


def verify_arguments(arg):
    # Check if file is CSV
    if arg.lower().endswith('.csv'):
        # Check if file exists
        if os.path.exists(arg):
            return True
        else:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
