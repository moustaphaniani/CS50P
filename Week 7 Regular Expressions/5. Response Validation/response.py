import validators

if __name__ == "__main__":

    email = input("What's your email address? ")

    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")
