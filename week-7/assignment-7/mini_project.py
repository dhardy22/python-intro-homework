'''

Part 2: Mini-Project — Expense Report Generator

The file ../data/expenses.csv tracks personal spending across several categories:

date,category,description,amount
2024-03-01,Food,Grocery store,54.30
2024-03-02,Transport,Bus pass,35.00
...
Write a program that analyzes this data and writes a formatted report to a new file. Follow these steps:

1. Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
2. Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
3. Convert the amount field to float for each row.
4. Filter the list to only rows where category is "Food".
5. Calculate the total amount spent on Food.
6. Write a report to food_report.txt with this structure:
    First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
    One line per food expense: [date]: $[amount]
    Last line: Total: $[total to 2 decimal places]

    Hint: All values from csv.DictReader come back as strings. Remember to convert amount with float() before doing any math.
Extension (optional, ungraded): Modify your program to work for any category, not just "Food". Running it for "Transport" should produce a transport_report.txt with the same format.
Save as: mini_project.py (and include food_report.txt to show your output)

'''

import csv
import datetime
import os
import sys

'''
Build an absolute path to the CSV so the script works no matter
what directory it's run from (not just from inside this folder)'''

file_path = "../data/expenses.csv"

if not os.path.exists(file_path):       # message if the file is missing and exit the program

    print("Error: File not found")
    sys.exit()

with open(file_path, newline="") as file:           # Read the CSV into a list of dictionaries (one dict per row)

    expenses = list(csv.DictReader(file))

''' DictReader gives every value as a string, so convert
"amount" to a float for each row before we can do math with it
'''

for expense in expenses:
    expense["amount"] = float(expense["amount"])

food_expenses = [expense for expense in expenses if expense["category"] == "Food"]  # list comprehension to filter the list to only rows where category is "Food"

total = sum(expense["amount"] for expense in food_expenses)     # Add up the amount across the filtered Food expenses


# Format today's date the way the report requires, e.g. "Month DD, YYYY"
today = datetime.date.today().strftime("%B %d, %Y")

# Format the report to food_report.txt
with open('food_report.txt' , 'w') as report:
    report.write(f"Food Expense Report — generated {today}\n")
    for expense in food_expenses:
        report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")
    report.write(f"Total: ${total:.2f}\n")


