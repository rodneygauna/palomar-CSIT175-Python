

def main():
    print("Assignment 4\n")
    
    while True:
        global first_name
        first_name = input("What is your first name? ")

        if is_field_blank(first_name):
            while True:
                global last_name
                last_name = input("\nWhat is your last name? ")

                if is_field_blank(last_name):
                    while True:
                        global user_age
                        age = input("\nWhat is your age? ")

                        if is_field_a_number(age) == True:
                            user_age = int(age)
                            if user_age > 40:
                                print("\nWell,", first_name, last_name, "it looks like you are over the hill")
                                print("\nEND OF ASSIGNMENT 4")
                                return True
                            else:
                                print("\nIt looks like you have many programming years ahead of you", first_name, last_name,)
                                print("\nEND OF ASSIGNMENT 4")
                                return True
                        else:
                            print("Age must be a Number")
                            continue
                else:
                    print("Last Name must be Entered")
                    continue
        else:
            print("First Name must be Entered\n")
            continue


def is_field_blank(name):
    if name.lower() != "":
        return True
    else:
        return False

def is_field_a_number(number):
    if number.isdigit() == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()