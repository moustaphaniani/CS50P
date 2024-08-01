# Prompt the user for a greeting
greeting = input("What's your greeting? ")

# Logic of the program
'''
If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
'''

if greeting.strip().lower().startswith("hello"):
    print("$0")
elif greeting.strip().lower().startswith("h"):
    print("$20")
else:
    print("$100")
