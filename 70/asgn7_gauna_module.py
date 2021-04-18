"""
This module if for Assignment 7.
There are 4 functions for this module:
payMe() - Prompts the user for a payment amount, validates the minium amount, displays an exceptions
getTarget() - Parses the user's entry of a question and checks for keywords (Who, What, Where, When, Why, or How), returns the frist keyword found or "unknown" if none
createList() - Search the A7_answers.txt file for the keyword passed from getTarget(), slice and split the text, return the list of answers
spinTheWheel() - Pass the user's name and the list from createList(), randomly select and pass the answer by dividing seconds and list count, prompt the user to spin the wheel, and return the answer
"""

import datetime

def payMe():
    """
    Prompts the user for a payment amount,
    Validates the minium amount,
    then Displays an exceptions
    """
    print("What's the most you are willing to pay me for my advice?\n")
    payment = input("The more you pay, the better the answer! (minimum price: $975.46) ")
    
    try:
        float_payment = float(payment)

        if float_payment >= 975.46:
            print("\nI guess", "${:,.2f}".format(float_payment), "seems like a fair price")
            return True
        else:
            print("\nGo Away!")
            return False

    except ValueError:
        print(f"You entered an invalid payment. It must be ####.## (example: 1234.56). The value could not convert the string to float: {payment}")

def getTarget(question):
    """
    Parses the user's entry of a question,
    Checks for keywords (Who, What, Where, When, Why, or How),
    then Returns the frist keyword found or "unknown" if none
    """    
    if "who" in question.lower():
        return "who"
    elif "what" in question.lower():
        return "what"
    elif "where" in question.lower():
        return "where"
    elif "when" in question.lower():
        return "when"
    elif "why" in question.lower():
        return "why"
    elif "how" in question.lower():
        return "how"
    else:
        return "unknown"

def createList(keywordTarget):
    """
    From getTarget() check the text file for that returned keyword,
    Parse the line from the text file,
    Split from the "*" character in the string,
    Append that line to display_list,
    then Return the list
    """
    display_list = []

    filename = "A7_answers.txt"

    with open(filename, "r") as file:
        for line in file:
            if keywordTarget in line.lower():
                display_list.append(line.split("*",1)[1].strip())
        return display_list

def spinTheWheel(name, list):
    """
    Receive the user's name and list from createList(),
    Get the total count of elements in the list,
    Store the count in a variable,
    Divide the list count by the current time (seconds),
    Using the remainder, store that index number fom createList() in an answer variable,
    Prompt the user to spin the wheel and display some "spinning" text,
    then Return the answer
    """
    
    countList = len(list)

    time = datetime.datetime.now()
    seconds = time.second

    randomItem = seconds % countList
    message = list[randomItem]

    while True:
        userSpins = input("\nPress ENTER to Spin the Wheel")
        
        if userSpins.lower() == "":
            break
        else:
            continue
    
    print("\nSpin..Spin..Spin....Spin.......Spin........tick, tick, tick, stop")
    return print(f"\nAttention {name}! The Wizard delcares: {message} \n")