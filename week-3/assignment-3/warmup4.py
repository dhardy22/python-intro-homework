# Ask the user for a number. Using two separate if/elif/else blocks — one for sign, one for parity — print two lines of output:

#User input for a number

number = int(input("Please enter a number: "))

#conditional block #1 tests even or odd

if number < 0 and number != 0 :
    print(f"{number} is negative")
elif number > 0 and number != 0 :
    print(f"{number} is positive")

#conditional block #2 tests number parity

if number % 2 == 0 and number != 0 :
    print(f"{number} is even")
elif number % 2 == 1 and number != 0 :
    print(f"{number} is odd")

# zero case

if number == 0 :
    print("0 is zero")
    print("0 is even")