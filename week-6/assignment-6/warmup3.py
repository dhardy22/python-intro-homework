'''
Define a variable inside a function. Try to access it outside the function
and show the NameError — paste the error in a comment, then remove or comment 
out the line that causes it.
'''
def calculate_total():
    total = 42  # 'total' only exists inside this function's local scope
    print(f"Inside the function, total is {total}")


calculate_total()

'''
Trying to access 'total' outside the function fails, because it never existed
outside the function's local scope:

print(total)

Traceback (most recent call last):
  File "warmup3.py", line 6, in <module>
    print(total)
NameError: name 'total' is not defined
'''

# Show how return solves the problem: return the value from the function and
# assign it to a variable in the outer scope. Print it to confirm it worked.

def calculate_total_fixed():
    total = 42
    return total


result = calculate_total_fixed()
print(f"Outside the function, result is {result}")