numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")
    print(f"DEBUG: you entered {repr(choice)}")   # temporarily add this line

    if choice == "1":
        smallest = numbers[0]  #  gives us a starting point for the smallest variable
        for number in numbers:  # variable 'number' rotates through the numbers list
            if number < smallest:
                smallest = number  # replaces the value of smallest if the inequality evaluates to True
        print(f"The minimum is: {smallest}")
        pass
    elif choice == "2":
        largest = numbers[0]  #start with a guess 
        for number in numbers:
            if number > largest:
                largest = number
        print(f"The maximum is: {largest}")
        pass
    elif choice == "3":
        found = False
        index = 0
        query = int(input("Enter a number to search for: "))
        while index < len(numbers):
            if numbers[index] == query:
                print(f"Found {query} at index {index}")
                break
            index += 1
        else:
            print(f"{query} not found in numbers")
        pass

    elif choice == "4":
        n = len(numbers)
        for i in range(n-1):
            for j in range(n-i-1):
                if numbers[j] > numbers[j+1]: #if the value of position [1] is greater than position [1+1] swap them
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        print(numbers)
        pass
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-5.")