# check if the filename exists
while True:
    # capture the the filename from the user
    file_name = input("What file do you want to open? ")

    try:
        with open(file_name, "r") as file:
            # if the filename exists, print out "Your file (file name) is there"
            print(f"Your file {file_name} is there.")
            break
    # if the filename doesn't exist, explain it can't be found and have them try again
    # use the FileNotFoundError exception
    # also, add the error message from the exception
    except FileNotFoundError as e:
        print("Your file myfile.txt has the following error:", e)
        continue
    finally:
        print("\nI would release resources here, if I had any")
        print("\nThanks!")