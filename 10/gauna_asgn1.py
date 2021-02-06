# Assignment 1
# Rodney Gauna // February 5, 2021
# Please carefully read the Instructions and Grading Criteria.
# Write a program that determines approximately how many years of your life you have been asleep.
# Name your program yourlastname_asgn1.py  (obviously, replace "yourlastname" with your last name!)
# 1. Collect the name, age, and number of hours they sleep entered by the user into program variables
print("Assignment 1")
print("")
print("What is your name? (Example: John)")
users_name = input()
print("How old are you, " + users_name + "? (Example: 21)")
users_age = int(input())
print("About how many hours of sleep would you get per night? (Example: 7)")
hours_slept = int(input())

# 2. Use the following conceptual formula to determine how many years of their life has been wasted sleeping... wasted_years = (hours_slept/24) * users_age
wasted_years = (hours_slept/24) * users_age

# 3. Round the wasted_years result to two decimal places
wasted_years_rounded = round(wasted_years, 2)

# 4. Format a string message that is in the following format...
#   Hello Steve.
#   You have been unconscious for 18.33 years!
# 5. Print the message on the console
print("")
print("Hello " + users_name + ".")
print("You have been unconscious for " + str(wasted_years_rounded) + " years!")
