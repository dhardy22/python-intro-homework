# raw_text = "Edmund Ashley Dorothy Alessandro Leanna Brycen Dandre Kale Jayna Ivy Jaime Augustine Karime Megan Brenden Debra Cameron Moses Luca Jase Malcolm John"

# clean_text = raw_text.replace("$1","")

# name_list = clean_text.split()

# print(name_list)

names = ['Edmund', 'Ashley', 'Dorothy', 'Alessandro', 'Leanna', 'Brycen', 'Dandre', 'Kale', 'Jayna', 'Ivy', 'Jaime', 'Augustine', 'Karime', 'Megan', 'Marcus', 'Brenden', 'Debra', 'Cameron', 'Moses', 'Luca', 'Jase', 'Malcolm', 'John']

query = input("Enter a name to search for: ") #here is the search target 
index = 0  #starts scanning from the first position

while index < len(names):  #only check valid positions - stop before running off the list 
    if names[index] == query: #checks the current index slot against the target 'query'
        print(f'Found "{query}" at index {index}') # index still holds the matching position
        break # stops scanning at the current index
    index += 1 # no match, move to the next position
    
else:
    print(f'"{query}" was not found in the list.') # index reached len(names) without a match

