#copy of the student list from roster.py. The list has 8 dictionairies 

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

total_score = 0      # Gives a fresh starting point for the total_score variable that we can iteratively add to.
top_score = None    #Sets equal to None because the variable is a placeholder and has the ability to change.
top_score_name = None #Creates a placeholder for top_score_name
subjects = set()   #Creates a new empty set that we will loop .add to from the item in students 
high_scorers = []

for item in students : 
    # Assigns current_score to the values using the item["key"]
    current_score = item["score"]
    #Since we've defined total_score as a variable starting @ 0 . we accumulate the score value over each pass of item in students
    total_score = total_score + item["score"]

    subjects.add(item["subject"])

    if top_score is None or current_score > top_score:

        top_score = current_score

        top_score_name = item["name"]

    if current_score > 75 :
        high_scorers.append(item["name"])


class_avg = (total_score)/(len(students))

print(f"Top scorer: {top_score_name} ({top_score})")

print(f"Class average: {class_avg}") 

print(f"Subjects offered: {subjects}") 

print(f"High scorers: {high_scorers}")

