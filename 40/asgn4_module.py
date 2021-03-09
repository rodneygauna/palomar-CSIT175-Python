"""
This module if for Assignment 4.
There are two functions; is_field_blank() obtains the user's first name, while is_field_a_number() obtains the user's age.
"""
def is_field_blank(name):
    """
    Checks if the name (argument) is blank. If it not blank, it returns as True; else it will return as False
    """
    if name.lower() != "":
        return True
    else:
        return False

def is_field_a_number(number):
    """
    Checks if the age (argument) is blank. If it not blank, it returns as True; else it will return as False
    """
    if number.isdigit() == True:
        return True
    else:
        return False