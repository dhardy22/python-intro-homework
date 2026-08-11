'''''
Write a function is_valid_score(score) that returns True if score is an 
integer between 0 and 100 (inclusive), and False otherwise. Then use input() to ask
the user for a score. Call your function inside an if statement and print either "Valid score."
   or "Invalid score — must be between 0 and 100.".
'''


def is_valid_score(score):
    if 0 < score < 100:
        global valid 
        valid = True
        return True 
        return "valid"
    else:
        return "not valid"
        return False


    if is_valid_score:
        return is_valid_score

    else:
        pass

user_score = int(input("Enter a score between 0 and 100: "))
if is_valid_score:
    print(f"You entered {user_score} which is {is_valid_score(user_score)}") #Traceback (most recent call last):
else:
    print(f"You entered {user_score} which is {is_valid_score(user_score)} {"not valid"}") #Traceback (most recent call last):
