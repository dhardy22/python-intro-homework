# Ask the user for a number. Using two separate if/elif/else blocks — one for sign, one for parity — print two lines of output:

#User input for a number

number = int(input("Enter a number: "))

#conditional block #1 number can either be less than or greater than 0 to satisfy one of the first two branches
#if the number is neither less than nor greater than 0, the number has to be zero

if number < 0 :
    print(f"{number} is negative.")
elif number > 0  :
    print(f"{number} is positive.")
else:              #If the number is neither greater than nor less than zero, the only number left is zero.
    print(f"{number} is zero.")

# #conditional block #2 tests number parity by dividing the number by two and checking if the remainder is 0 or 1.
# #If the number does not have a remainder, the first branch of the block is true so it runs
# #If the number has a remainder it fails the first branch the else branch will run. 

if number % 2 == 0 :
    print(f"{number} is even.")
else  :
    print(f"{number} is odd.")


