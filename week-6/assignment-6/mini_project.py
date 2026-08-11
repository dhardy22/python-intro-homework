def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = int(input("Choose an option (1-5): "))
    # print(f"DEBUG: you entered {repr(choice)}")   # temporarily add this line
    return choice

def find_min(nums):  #  reserves the first position for the smallest value
        smallest = nums[0]
        n = len(nums)
        for index in range(n):  # variable 'number' rotates through the numbers list
            if nums[index] < smallest:
                smallest = nums[index]  # replaces the value of smallest if the inequality evaluates to True
        return smallest
'''Find Maximum '''
def find_max(nums):
        largest = nums[0]  # reserves the first position largest 
        n = len(nums)
        for index in range(n):
            if nums[index] > largest:
                largest = nums[index]
        return largest 

'''Review help from Claude'''
def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1

def bubble_sort(numbers):
    sorted_list = numbers.copy()
    n = len(sorted_list)
    indexing_length = n - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(indexing_length):
            if sorted_list[i] > sorted_list[i + 1]:
                is_sorted = False
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
    return sorted_list
         
     
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def main():
    while True:

        choice = show_menu()

        if choice == 1:
            print(f"\n The minimum is: {find_min(numbers)} \n")
            pass

        elif choice == 2:
            print(f"\n The maximum is: {find_max(numbers)} \n")
            pass

        elif choice == 3:
                try:
                    query = int(input("\nEnter a number to search for: "))
                except ValueError:
                            print("That's not an integer. Try again.")
                else:
                    index = search(numbers, query)
                    if index != -1:
                        print(f"\nFound {query} at index {index}\n")
                    else:
                        print(f"\n{query} not found in numbers\n")


        elif choice == 4:
            print(f"\n{bubble_sort(numbers)}\n")


        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

main()


    
