while True:
    items = input("Enter an item for your grocery list: ")

    if items.lower() == "":
        print("\nGrocery List:\n")
        with open("60-3-txt.txt", "r") as file:
            contents = file.read()
            print(contents)
        break
    else:
        with open("60-3-txt.txt", "a") as file:
            file.write(items + "\n")
        continue