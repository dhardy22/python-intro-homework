#hard coded list of 8 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#print the first item
first = numbers[0]
print(f"First: {first}")

#print the last item
last = numbers[-1]
print(f"Last: {last}")

#print the middle 4 numbers
middle = numbers[2:6]
print(f"Middle: {middle}")

#print the list in reverse order
backwards = list(reversed(numbers))
print(f"Reversed: {backwards}")
