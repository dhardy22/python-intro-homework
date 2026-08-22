'''
1. Use try/except FileNotFoundError to check that the file exists before opening it. If not, print an error and stop.
2. Read the file with csv.DictReader.
3. Process each row inside a try/except block. Catch at minimum:
   ValueError — when amount can't be converted to float
   KeyError — when an expected column is missing from a row
4. Collect successfully parsed rows into a list of dictionaries.
5. Print a summary at the end:'''

#EXAMPLE OUTPUT
'''=== CSV Report ===
Rows attempted:  14
Rows parsed:      9
Rows skipped:     5

Skipped rows:
  Row 3: ValueError — could not convert '' to float
  Row 5: ValueError — could not convert 'not_a_number' to float
  Row 7: extra column detected — skipped
  Row 11: ValueError — could not convert '' to float
  Row 13: ValueError — could not convert 'fifteen' to float

Clean data:
  Alice | Food | $12.50
  Bob | Transport | $8.75
  ...'''

import csv

file_path = '../data/messy_data.csv'     

try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        rows_attempted = 0
        rows_parsed = 0
        rows_skipped = 0
        skipped_rows = []
        clean_data = []     

        for row in reader:
            rows_attempted += 1
            try:
                # Attempt to process the row
                amount = float(row['amount'])  # This may raise ValueError
                clean_data.append(row)
                rows_parsed += 1
            except ValueError as ve:
                skipped_rows.append(f"Row {rows_attempted}: ValueError — could not convert '{row.get('amount', '')}' to float")
                rows_skipped += 1
            except KeyError as ke:
                skipped_rows.append(f"Row {rows_attempted}: KeyError — missing expected column '{ke.args[0]}'")
                rows_skipped += 1

    # # Format the report to food_report.txt
    # with open('food_report.txt' , 'w') as report:
    #     report.write(f"Food Expense Report — generated {today}\n")
    # for expense in food_expenses:
    #     report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")
    # report.write(f"Total: ${total:.2f}\n")

    print("File read successfully.")
except FileNotFoundError:
    print(f'Error: "{file_path}" was not found. Please check the file path and try again.')

print(f"=== CSV Report ===")
print(f"Rows attempted:  {rows_attempted}")
print(f"Rows parsed:      {rows_parsed}")
print(f"Rows skipped:     {rows_skipped}\n")
if skipped_rows:
    print("Skipped rows:")
    for skipped in skipped_rows:
        print(f"  {skipped}")   
        