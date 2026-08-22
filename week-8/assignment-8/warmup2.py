#script to divide two numbers with exception handling
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")
except ValueError:
    print("Please enter valid numbers")
else:
   print(f"{numerator} ÷ {denominator} = {result}")




