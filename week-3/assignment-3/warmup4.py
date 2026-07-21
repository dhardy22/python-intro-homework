# Ask the user for a number. Using two separate if/elif/else blocks — one for sign, one for parity — print two lines of output:

#User input for a number

number = int(input("Enter a number: "))

#conditional block #1 tests even or odd and zero case

if number < 0 :
    print(f"{number} is negative.")
elif number > 0  :
    print(f"{number} is positive.")
else:              #If the number is neither greater than nor less than zero, the only number left is zero.
    print(f"{number} is zero.")

#conditional block #2 tests number parity and zero case

if number % 2 == 0 :
    print(f"{number} is even.")
else  :
    print(f"{number} is odd.")


