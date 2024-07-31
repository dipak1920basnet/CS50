from validator_collection import checkers

def main():
    get_email = input("What's your email address? ")
    t = check(get_email)
    # Printing email valid or invalid
    if t == True:
        print("Valid")
    else:
        print("Invalid")


# Checking if email is valid
def check(s):
    t = checkers.is_email(s)
    return t

if __name__ == "__main__":
    main()

