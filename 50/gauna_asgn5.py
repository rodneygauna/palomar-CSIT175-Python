# import the random function
import random

# List of programming names
coding = ["Python", "JavaScript", "PHP"]

def main():
    print("Assignment 5\n")
    print("List of Classes | Teach:\n")
    displayMyClasses(coding)
    # Allow the user to add or remove items from the list
    while True:
        more_code = input("\nDo you need to Add or Remove a class? (A/R) ")

        # If input is blank/null, exit the loop
        if more_code.lower() == "":
            print("\nList of Classes I Teach:")
            displayMyClasses(coding)
            guessNext(coding)
            print("\nEND OF ASSIGNMENT 5")
            break
        else:
            # If input is "A", add to the list
            if more_code.lower() == "a":
                add_code = input("\nEnter the name of the class you wish to add: ")
                coding.append(str(add_code))
                continue
            # If input is "R", remove from the list
            elif more_code.lower() == "r":
                remove_code = input("\nEnter the name of the class you wish to remove: ")
                coding.remove(remove_code)
                continue
            else:
                print("\nYou must choose an 'A' to Add or an 'R' to Remove a class")
                continue
            

def displayMyClasses(c_list):
    """
    Takes the argument (a list), sorts the items, and prints it as a numbered list
    """
    count = 0
    c_list.sort()
    for code in c_list:
        count = count + 1
        print(str(count) + ".", code)

def guessNext(program):
    """
    Takes the argument (a list) and prints one randomly
    """
    print("\nThe next class you should teach is:", random.choice(program))

if __name__ == "__main__":
    main()