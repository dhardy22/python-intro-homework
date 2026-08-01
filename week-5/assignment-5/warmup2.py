#Use a while loop that repeatedly asks the user to enter a positive integer. If the user enters anything that isn't a positive integer, print a message and ask again. Once valid input is received, print it and stop:


while True:
    try: #tells the program what to do when it encounters a runtime error
        number = int(input("Enter a positive integer: ")) 
    except ValueError: # when the input is not an integer ValueError will be replaced by the print statement
        print("That's not a positive integer. Try again.")
        continue

    if number > 0: #if number is a positive integer print the statement. Break the while loop.
        print(f"Got it: {number}")
        break

    print("That's not a positive integer. Try again.")
