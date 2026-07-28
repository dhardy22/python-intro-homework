# Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings). Then:
# Print each key-value pair using .items() in a for loop
# Add a new key "graduated" with the value False
# Print the updated dictionary

students = {
    "name":"Cindy", 
    "grade":"A+", 
    "subjects":["Maths", "Literature", "Chemistry", "History"]
    }

for key, value in students.items():
    print(f"Key:{key} | Value:{value}")
