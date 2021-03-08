"""
This module if for Assignment 4.
There are two functions; is_field_blank() obtains the user's first name, while is_field_a_number() obtains the user's age.
"""
def is_field_blank():
    """
    This function takes the user's first name.
    If the user enters nothing, it will post an error and continue to prompt till something is entered.
    """
    while True:
        global first_name
        first_name = input("What is your first name? ")

        if first_name.lower() != "":
            while True:
                global last_name
                last_name = input("\nWhat is your last name? ")

                if last_name.lower() != "":
                    return last_name
                else:
                    print("Last Name must be Entered")
                    continue
            return first_name
        else:
            print("First Name must be Entered\n")
            continue

def is_field_a_number():
    """
    This fuciton takes the user's age.
    If the user enters nothing or the entry isn't a number (digit), it will post an error and continue to prompt till something is entered.
    """
    while True:
        global user_age
        age = input("\nWhat is your age? ")

        if age.isdigit() == True:
            user_age = int(age)
            return user_age
        else:
            print("Age must be a Number")
            continue