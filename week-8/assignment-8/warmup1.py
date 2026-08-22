validated = False #creates a conditional variable to check if the user input is valid

while not validated:
    try:
        user_num = float(input("Enter a number: "))
    except ValueError:
        print("That's not a valid number. Try again.")
    else:
        print(f"You entered: {user_num}")
        validated = True #when the input is valid, the conditional variable is set to True and the loop ends

