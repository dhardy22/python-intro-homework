#Hard coded variable for score setting it equal to what ever number is to the right of the equal sign.
score = 84 

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}\nGrade: {grade}")