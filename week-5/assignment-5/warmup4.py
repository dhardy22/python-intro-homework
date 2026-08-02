
numbers = 0 # gives us a starting point for numbers in the given range. In this case just less than the range length

while numbers < len(range(1,31)): # constrains the loop to only numbers within the given range
    for numbers in range(1,31): 
        if numbers % 3 == 0 and numbers % 5 == 0: #checks the combined case of divisible by 3 and 5
            print("FizzBuzz")
        elif numbers % 3 == 0: #checks for instances divisible by 3
            print("Fizz")
        elif numbers % 5 == 0: #checks for instances divisible by 5
            print("Buzz")
        else:                   #prints the number otherwise
            print(numbers)

