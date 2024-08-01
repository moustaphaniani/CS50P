# Program that:
#
# 1. Expects the user to provide two command-line arguments:
#    a) the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
#    b) the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# 2. Converts that input to that output, splitting each name into a first name and last name.
#    Assume that each student will have both a first name and last name.
#
# If the user does not provide exactly two command-line arguments, or if the first cannot be read,
# the program should exit via sys.exit with an error message.

import os
import os.path
import sys
import csv

def main():
    # Verify if al least 2 argument are passed
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # Verify if more than 2 argument are passed
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Only chance to have is 2 arguments passed
    else:
        if verify_arguments(sys.argv[1]):
            create_output_file(sys.argv[1], sys.argv[2])


def verify_arguments(arg):
    # Check if file is CSV
    if arg.lower().endswith('.csv'):
        # Check if file exists
        if os.path.exists(arg):
            return True
        else:
            sys.exit(f"Could not read {arg}")
    else:
        sys.exit("Not a CSV file")


def create_output_file(file_in, file_out):
    new_rows = []
    content = [['first', 'last', 'house']]
    # Open file, read content and close file
    with open(file_in) as csvfile:
        reader = csv.reader(csvfile)
        # Iterate throught each line and assign fullname and house
        for row in reader:
            new_rows.append([row[0], row[1]])
    # Delete header
    del new_rows[0]
    # Create new list [result] wit lastname, name and house
    for new_row in new_rows:
            last, first = new_row[0].split()
            content.append([first, last.replace('"', '').replace(' ', '').replace(',', ''), new_row[1]])
    # Open new file, write content and close file
    with open(file_out, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in content:
            writer.writerow(row)


if __name__ == "__main__":
    main()
