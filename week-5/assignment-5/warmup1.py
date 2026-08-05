
total = 0 #creates our updatable 'total' variable that we can add to in the loop

for i in range(1, 101): # tells the program that we want to head this for loop with variable i and interate 1 through 100
    total = total + i #each /iteration through the range will result in 'total' being updated by adding it to the total

print(f"The sum of 1 to 100 is {total}.")  # updated total can print each iterated total if nested inside the for loop
 