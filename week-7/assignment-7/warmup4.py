'''
Print today's date in the following format:

Today is April 24, 2026.
Use datetime.now() and .strftime().
Save as: warmup4.py

'''

from datetime import datetime

now = datetime.now()

print(f"Today is {now.strftime('%B %d, %Y')}")