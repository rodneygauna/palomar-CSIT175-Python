import asgn4_module as func

def main():
    print("Assignment 4\n")
    func.is_field_blank()
    func.is_field_a_number()
    
    if func.user_age > 40:
        print("\nWell,", func.first_name, func.last_name, "it looks like you are over the hill")
        print("\nEND OF ASSIGNMENT 4")
    else:
        print("\nIt looks like you have many programming years ahead of you", func.first_name, func.last_name,)
        print("\nEND OF ASSIGNMENT 4")

if __name__ == "__main__":
    main()