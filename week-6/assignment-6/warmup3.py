#Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then remove or comment out the line that causes it.

def my_functino(variable):
    result = variable + 23
    return result

print(f"{variable} + 23 = {my_functino(22)}") #Traceback (most recent call last):
#   File "/Users/donovanhardy/CTD/python_class/python-intro-homework/week-6/assignment-6/warmup3.py", line 7, in <module>
#     print(f"{variable} + 23 = {my_functino(22)}") #Traceback (most recent call last):
#              ^^^^^^^^
# NameError: name 'variable' is not defined. Did you mean: 'callable'?
 
# Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.
