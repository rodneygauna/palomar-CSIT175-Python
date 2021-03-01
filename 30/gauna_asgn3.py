# Assignment 3

# 1. Prompt the user to enter your name.
# 2. Then prompt the user to enter the names of your three best friends
# 3. Then list those friends in the format shown in the "Sample Program" below
# 4. Then prompt the user to enter the names of other wedding guests.
# 5. When completed with entering names, display the list of attendees in the format shown in the "Sample Program" below
# 6. Follow the format of the "Sample Program below with the first and last lines appearing as shown. Also, be sure to use line skipping and spacing the way I show below.
print("Assignment 3\n")

name = input("What is your name? ")
print("")

friend_output = ""
print("Please Enter the name of your three best friends\n")

for ff in range(1,4):
    friend = input("Enter Friend Name: ")
    friend_output = friend_output + str(ff) + ". " + friend + "\n"

print("\nMy Best Friends are:")
print(friend_output)

guests_output = ""
counter = 0
print("Now enter the names of other people you are inviting to your wedding\n")

while True:
    guest = input("Guest's Name (or press Enter to quit): ")

    if guest.lower() == "":
        break
    else:
        counter = counter + 1
        guests_output = guests_output + str(counter) + ". " + guest + "\n"
        continue

print("\nMy Wedding Attendees are:")
print(guests_output)

print("\nEND OF ASSIGNMENT 3")
