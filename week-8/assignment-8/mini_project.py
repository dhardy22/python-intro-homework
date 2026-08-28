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

        #row-by-row error handling
        for row in reader: # for each row of our list of dictionaries, do the following
            rows_attempted += 1 #first thing is to increment the rows_attempted counter by 1

            #checks for extra columns (values without headers)
            if row.get(None): # Puts the values without headers into a list with the key None.
                skipped_rows.append(f"Row {rows_attempted}: extra column detected — skipped") #this appends the f string (with our row # from rows_attempted)to the end of the skipped_rows =[] list  
                rows_skipped += 1 # adds 1 to the rows_skipped count if the row has values without headers
                continue # continues to the next line if the row has values without headers
            try:
                # Attempt to process the row
                amount = float(row['amount'])  # typecasts the values associated with amount to a float. May cause Value error if the value is not a number.
                row['amount'] = amount  # Assigns the converted values back to the key 'amount' in the row/dictionary
                clean_data.append(row) # adds our converted dictionaries (row) to a new list called cleaned_data 
                rows_parsed += 1 #adds 1 to our rows parsed counter if the conversion was successful - try: handles the operation without breaking if the conversion does not work
            except ValueError as ve: 
                skipped_rows.append(f"Row {rows_attempted}: ValueError — could not convert '{row.get('amount', '')}' to float") # adds the error message to the skipped_rows list
                rows_skipped += 1 # adds 1 to the rows_skipped counter if ValueError occurs
            except KeyError as ke:
                skipped_rows.append(f"Row {rows_attempted}: KeyError — missing expected column '{ke.args[0]}'") #runs if KeyError occurs - appends the f-string with the key that could not be mapped
                rows_skipped += 1 # adds 1 to the rows_skipped counter if KeyError occurs

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

