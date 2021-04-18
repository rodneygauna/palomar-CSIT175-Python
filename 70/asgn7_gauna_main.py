import asgn7_gauna_module as func
import datetime

def main():
    print("* * The Wizard * *\n")
    print("The Wizard will see you now\n")

    if func.payMe() == True:
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
            keepGoing = input("\nDo you have another question? Y/N ")

            if keepGoing.lower() == "y":
                askWizard = input("\nWhat's your question? ")

                if askWizard.lower() == "":
                    continue
                else:
                    word = func.getTarget(askWizard)
                    answerList = func.createList(word)
                    func.spinTheWheel(name, answerList)
            
            elif keepGoing.lower() == "n":
                time = datetime.datetime.now()
                numDay = str(time.day)
                numLast = numDay[-1]
                numSuffix = ""
                if numLast == "1":
                    numSuffix = "st"
                elif numLast == "2":
                    numSuffix = "nd"
                elif numLast == "3":
                    numSuffix = "rd"
                else:
                    numSuffix = "th"
                print("\nOn this day,", time.strftime("%A") + ", the", time.strftime("%d") + numSuffix + " in the month of", time.strftime("%B"), "in the year of", time.strftime("%Y"))
                print("The Wizard wants you to go away now!")
                break

if __name__ == "__main__":
    main()