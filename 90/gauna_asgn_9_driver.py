import gauna_asgn_9_module as cars
from random import randint

def main():
    myCar = cars.Model_1()
    computerCar = cars.Model_2()
    
    print("Let the Race Begin!\n")

    print("* * The first car to 50 wins * *\n")

    print("Your car is Model 1 and the color is " + myCar.getColor())
    myCar.soundHorn()

    print("\nThe computer's car is Model 2 and the color is " + computerCar.getColor())
    computerCar.soundHorn()
    print()

    while True:
        if int(myCar.distance) >= 50:
            print("You Win!")
            leave = input("\nPress Enter to Leave Program ")

            if leave.lower() == "":
                break
            else:
                continue
        elif int(computerCar.distance) >= 50:
            print("The Computer Wins!")

            leave = input("\nPress Enter to Leave Program ")

            if leave.lower() == "":
                break
            else:
                continue
        else:
            keepGoing = input("Drive some more? (y/n) ")

            if (keepGoing.lower() == "y" or keepGoing.lower() == ""):
                print()
                randNum_MyCar = randint(1, 5)
                myCar.showLine(randNum_MyCar)
                print(f"({myCar.getColor()}) {myCar.line}> ({int(myCar.distance)})")

                randNum_ComputerCar = randint(1, 5)
                computerCar.showLine(randNum_ComputerCar)
                print(f"({computerCar.getColor()} ) {computerCar.line}> ({int(computerCar.distance)})")
                continue
            elif keepGoing.lower() == "n":
                break

if __name__ == "__main__":
    main()