# generic membership eligibility questionaire
# User inputs: name, age , citizenship , and compliance  
name = input("What is your name?: ")
age = int(input("How old are you?: "))
is_citizen = input("Are you a citizen? (yes/no): ").lower()
is_compliant = input("Do you agree to the code of conduct? (yes/no): ").lower()

if age < 18:
    print("Sorry, " + name + ", you must be at least 18 years old to apply for membership.")
elif is_citizen == "no" or is_compliant == "no":
    print("Sorry, " + name + ", you do not meet the membership requirements.")
else:
    print("Hello " + name + ", you are eligible to apply for membership")


