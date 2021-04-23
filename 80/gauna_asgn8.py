def main():
    print("Assignment 8\n")

    names = {}

    # parse the text file and build dictonary of first:last
    filename = "A8_names.txt"

    with open(filename, "r") as file:
        for line in file:
            lastname = line.split("*",1)[1].strip()
            firstname = line.split("*",1)[0].strip()
            
            # add to the dictory
            names[firstname] = lastname

    # sort the dictory by key
    names_list = list(names.keys())
    names_list.sort()
    for name in names_list:
        print(name, names[name])

    while True:
        name_search = input("\nWhat is the first name you are looking for? ")

        if name_search == "":
            break
        else:
            if name_search in names:
                print("\nYour full name is:", name_search, names[name_search])
            else:
                print(f"\nI was unable to find {name_search} in the list")
    
    print("End of Program")

if __name__ == "__main__":
    main()