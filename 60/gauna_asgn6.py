# todo: fix formatting of output

# step 1 - import os
import os

# step 2 - empty list
item_list = []
convert_item_list = []

# step 3 - main function that does the rest of the steps
def main():
    # step 4 - calls os module and removes the costlist.txt file if it exists
    if os.path.exists("costlist.txt"):
        os.remove("costlist.txt")
    
    #step 5 - displays "Assignment 6"
    print("Assignment 6\n")
    
    while True:
        # step 6 - prompt user to enter a file name
        file_name = input("Enter file name ")

        # step 6a - if file name entered is "end", end the program
        if file_name == "end":
            print("Program Ended")
            break
        # step 6b-1 - if file name entered is "items.txt read the file,
        else:
            try:
                with open(file_name, "r") as file:
                    print("")
                    # step 6b-2 - replace the breakline with an empty string,
                    # step 6b-3 - add the items to the list
                    for line in file:
                        item_list.append(line.strip())
                    # step 7 - sort the list
                    item_list.sort()
                    # step 8a-1 - for each element in the list, prompt the user to enter the price
                    for item in item_list:
                        price = input(f"How much should {item} cost? ")
                        # step 8a-2 - convert the number into a float
                        while True:
                            try:
                                # step 8a-4 - continue with the next item
                                f_price = float(price)
                                # step 8b-1 - if number converts, create string variable with the following format:
                                # step 8b-2 - "(element) have a cost of (cost) dollars"
                                item_cost = item + " have a cost of " + str(f_price) + " dollars"
                                # step 8b-3 - open the costlist.txt file
                                with open("costlist.txt", "a") as file:
                                    # step 8b-4 - append and write the string created to a line in the file
                                    file.write(item_cost + "\n")
                                    break
                            # step 8a-3a - if number can't be converted, give ValueError exception,
                            except ValueError:
                                # step 8a-3b - display an error message
                                print(f"You entered an invalid float that could not convert string to float: {price} \nSkipping to the next item after {item}\n")
                                break
                with open("costlist.txt", "r") as file:
                    contents = file.read()
                    # step 9 - display "Cost List"
                    print("\nCost List\n")
                    # step 10 - display each line from the costlist.txt file
                    print(contents)
                    # step 11 - display "Program End"
                    print("\nProgram End")
                    break
            # step 6c - if FileNotFoundError exception, display the error and let the user try again
            except FileNotFoundError:
                print("Could not find file named", file_name + ". Please Try Again\n")
            
    
    



if __name__ == "__main__":
    main()