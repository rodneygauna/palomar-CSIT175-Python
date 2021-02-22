# Assignement 2
# Rodney Gauna // February 21, 2021
# Step 1.  Display "Assignment 2" and skip a line on the console
print("Assignment 2")
print("")
# Step 2.  Prompt the user for their first name with "What is your first name?" and skip a line on the console
firstname = input("What is your first name? ")
print("")
# Step 3.  If the first name entered is not blank, proceed to Step 4 below
#   If the first name entered is blank (i.e. the user presses the enter key but did not enter anything), prompt them again to enter their first name with "You are required to enter your first name" and skip a line on the console.
if firstname == "":
    firstname = input("You are required to enter your first name ")
    print("")
    #   If they entered a blank again, then display "Name is still missing, exiting program " and exit the program, otherwise the program should proceed to Step 4 below.
    if firstname == "":
        print("Name is still missing, exiting program ")
        exit()
# Step 4.  Display "Hi (firstname)"
#   Note:  Replace (firstname) with the the name the user entered above.
else:
    print("Hi " + firstname)
# Step 5.   Prompt the user for "What year were you born?" and skip a line on the console
year = input("What year were you born? ")
print("")
# Step 6.  Check to see if birth year entered is not numeric
if year.isnumeric():
    #   If the birth year entered is a valid number, then proceed to Step 7 below, otherwise display "Birth Year entered not Valid, exiting program" then exit the program,
    # Step 7. Prompt the user with "What city do you live in?" and skip a line on the console.
    city = input("What city do you live in? ")
    print("")
    #   Check the city value entered to see if it is either "Fresno" or "Bakersfield" (case-insensitive) and...
    if city.lower() == "fresno":
            #     ... if so, display "I'm sorry it's so hot where you live"]
            print("I'm sorry it's so hot where you live")
    elif city.lower() == "bakersfield":
            print("I'm sorry it's so hot where you live")
    #     ... if not, display "Hope you like it in (city entered)"
    else:
            print("Hope you like it in " + city)
#   If the birth year entered is a valid number, then proceed to Step 7 below, otherwise display "Birth Year entered not Valid, exiting program" then exit the program,
else:
    print("Birth Year entered not Valid, exiting program")
    exit()
# Step 8.  Skip a line on the console and display "END OF ASSIGNMENT 2"
print("")
print("END OF ASSIGNMENT 2")
# NOTE 1: Wherever I put something like (city entered) replace it with the variable that holds the city entered.
# NOTE 2: Wherever I use the word "prompt" it implies using the input() function. Wherever I use the word "display" it implies using the print() function.
