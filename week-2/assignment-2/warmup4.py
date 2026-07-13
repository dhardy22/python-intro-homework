name = input("what is your name?: ")

print(f"Hi {name}, time flies by fast.")
age = input("How old are you?: ")

add_tenyears = age + 10
print(f"In 10 years you will be {add_tenyears}.")


#1. What the error message said (paste it): Traceback (most recent call last):
#   File "/Users/donovanhardy/CTD/python_class/python-intro-homework/week-2/assignment-2/warmup4.py", line 6, in <module>
#     add_tenyears = {age + 10}
#                     ~~~~^~~~
# TypeError: can only concatenate str (not "int") to str
#2. What caused it: since age is a strings by default since it is an input, age, a string, could not be added to 10, an integer 
#3. How you fixed it: to fix it, i will typecast age to an integer.