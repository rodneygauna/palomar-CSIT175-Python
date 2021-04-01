mylist = []

while True:
    items = input("Enter an item for your grocery list: ")

    if items != "":
        mylist.append(items)
        continue
    else:
        mylist.sort()
        for item in mylist:
            with open("60-4-txt.txt", "a") as file:
                file.write(item + "\n")
        with open("60-4-txt.txt", "r") as file:
            contents = file.read()
            print("\nGrocery List:\n")
            print(contents)
            print("\nPROGRAM END")
        break
    