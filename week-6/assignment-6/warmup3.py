#Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then remove or comment out the line that causes it.

def is_valid_number(number):
    if 50 < number < 100:
        global valid 
        valid = True
        return True 
        return "valid"
    else:
        return "not valid"
        return False


    if is_valid_number:
        return is_valid_number
    else:
        pass

user_number = int(input("Enter a number between 50 and 100: "))
if is_valid_number:
    print(f"You entered {user_number} which is {is_valid_number(user_number)}") #Traceback (most recent call last):
else:
    print(f"You entered {user_number} which is {is_valid_number(user_number)} {"not valid"}") #Traceback (most recent call last):
#   File "/Users/donovanhardy/CTD/python_class/python-intro-homework/week-6/assignment-6/warmup3.py", line 7, in <module>
#     print(f"{variable} + 23 = {my_functino(22)}") #Traceback (most recent call last):
#              ^^^^^^^^
# NameError: name 'variable' is not defined. Did you mean: 'callable'?
 
# Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.
