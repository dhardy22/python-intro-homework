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
top_score = None    #
subjects = set()

for item in students : 
    current_score = item["score"]
    total_score = total_score + item["score"]
    # subjects.add(students["subject"])

    if top_score is None or current_score > top_score:
        top_score = current_score

class_avg = (total_score)/(len(students))




print(top_score)
print(class_avg) 
print(subjects)       