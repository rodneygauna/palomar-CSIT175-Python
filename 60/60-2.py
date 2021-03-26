firstname = input("What is your First Name? ")
lastname = input("What is your Last Name? ")

with open("60-2-txt.txt", "w") as file:
    file.write("Hi " + firstname + "\n")
    file.write("Your lastname is " + lastname + "\n")

print(file, "created")