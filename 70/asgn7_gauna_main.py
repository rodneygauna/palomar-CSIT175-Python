import asgn7_gauna_module as func
import datetime

def main():
    print("* * The Wizard * *\n")
    print("The Wizard will see you now\n")
    func.payMe()
    print("\nOK, let's get started\n")

    while True:
        global name
        name = input("What's your name? ")
        
        if name.lower() == "":
            continue
        else:
            break
    
    print("")
    
    while True:
        askWizard = input("What's your question? ")

        if askWizard.lower() == "":
            continue
        else:
            break
    
    word = func.getTarget(askWizard)
    answerList = func.createList(word)
    func.spinTheWheel(name, answerList)

    while True:
        keepGoing = input("Do you have another question? Y/N ")

        if keepGoing.lower() == "y":
            askWizard = input("What's your question? ")

            if askWizard.lower() == "":
                continue
            else:
                break
        
            word = func.getTarget(askWizard)
            answerList = func.createList(word)
            func.spinTheWheel(name, answerList)
        elif keepGoing.lower() == "n":
            time = datetime.datetime.now()
            # TODO if you have time, try to figure out when to add "st", "nd", "rd", and "th"
            print("On this day,", time.strftime("%A") + ", the", time.strftime("%d") + "th in the month of", time.strftime("%B"), "in the year of", time.strftime("%Y"))
            print("The Wizard wants you to go away now!")
            break

        


if __name__ == "__main__":
    main()