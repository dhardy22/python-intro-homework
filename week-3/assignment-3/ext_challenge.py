name = input("What is your name? ")
age = int(input("How old are you? "))
is_resident = input("Do you live in the city? (yes/no): ").lower()

if age < 5:
    print("Sorry, " + name + ", you must be at least 5 years old to get a library card.")
elif age < 18 and is_resident == "yes":
    print("Welcome, " + name + "! You qualify for a free Youth Card.")
elif age < 18 and is_resident == "no":
    print("Welcome, " + name + "! You qualify for a Youth Card ($5/year).")
elif age >= 65 and is_resident == "yes":
    print("Welcome, " + name + "! You qualify for a free Senior Card.")
elif age >= 65 and is_resident == "no":
    print("Welcome, " + name + "! You qualify for a Senior Card ($10/year).")
elif is_resident == "yes":
    print("Welcome, " + name + "! You qualify for a free Adult Card.")
else:
    print("Welcome, " + name + "! You qualify for an Adult Card ($25/year).")