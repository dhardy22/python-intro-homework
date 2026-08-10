#variables that can be passed through the function in the 
c = 100
c_2 = 0
f = 72

def celsius_to_fahrenheit(celsius): # tells python that i want celsius as the parameter of celsius_to_fahrenheit function
    fahrenheit = celsius * 9/5 + 32  #function statement: what i want done to the parameter
    return fahrenheit # returns the value to the function

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#Passes the variable as an argument inside the function and is called as a value inside the f string {}
print(f"{c_2}°C = {celsius_to_fahrenheit(c_2):.1f}°F")
print(f"{c}°C = {celsius_to_fahrenheit(c):.1f}°F")
print(f"{f}°F = {fahrenheit_to_celsius(f):.1f}°C")

    


