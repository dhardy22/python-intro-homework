# Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings). Then:
# Print each key-value pair using .items() in a for loop
# Add a new key "graduated" with the value False
# Print the updated dictionary

#creates a dictionary called students and stores {"key" : "value"} pairs
students = {
    "name" : "Cindy", 
    "grade" : "A+", 

    #gives the "subject" key the listed values. Remember, lists are stored square brakcets 
    "subjects" : ["Mathematics", "Literature", "Chemistry", "History"]
}

#prints each key, value pair in the dictionary using .items() to parse each pair    
for key, value in students.items():
    print(f"{key} {value}")

#creates a new "graduated" key, puts it inside of the dictionary students and sets it equal to the Boolean False 
students["graduated"] = False

#prints the updated dictionary 
print(students)


