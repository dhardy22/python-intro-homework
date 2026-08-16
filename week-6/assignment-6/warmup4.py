'''
Write a function is_valid_score(score) that returns True if score is an
integer between 0 and 100 (inclusive), and False otherwise. Then use input() to ask
the user for a score. Call your function inside an if statement and print either "Valid score."
or "Invalid score — must be between 0 and 100.".
'''


def is_valid_score(score):
    if isinstance(score, int) and 0 <= score <= 100:
        return True
    else:
        return False


raw_value = input("Enter a score between 0 and 100: ")

try:
    user_score = int(raw_value)
except ValueError:
    # Keep the raw (non-integer) value so is_valid_score can catch the type
    # failure itself, instead of the calling code filtering it out first.
    user_score = raw_value

if is_valid_score(user_score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")
