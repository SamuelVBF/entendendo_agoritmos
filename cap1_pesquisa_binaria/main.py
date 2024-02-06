import time

# This function performs a binary search on the input list for the specified item.
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    steps = 0

    print('-------------------BINARY SEARCH-------------------')

    while low <= high:
        mid = (low + high) // 2 # Find the middle of the range
        guess = lst[mid] # Is this our guy?
        steps += 1  # Keep track of how many comparisons we made

        print(f'low: {low}, high: {high}, mid: {mid}, guess: {guess} ------- step {steps}')

        if guess == item:  # Yes! We found it.
            return steps, time.perf_counter() # Return the index position  and number of steps taken to find it
        elif guess > item:  # Nope, the target is lower than mid.
            high = mid - 1    # Continue to search in the left subarray.
        else:
            low = mid + 1      # The target is higher than mid, so search the right subarray.

    print(f'Could not find "{item}" in list')
    return None #  Item was not found in the list.

 # This function performs a simple search on the input list for the specified item.
def simple_search(lst, item):
    first = 0
    target = len(lst) - 1
    steps = 0

    print('\n-------------------SIMPLE SEARCH-------------------')

    while first != target:
        steps += 1 #  Increment number of steps taken
        current = first + 1 #  Get the next element from the list

        print(f'kick: {first} ---------- step {steps}') #  Debugging information

        if lst[current] == item: #  Found the item at the next location
            return steps, time.perf_counter()  # Return the number of steps and elapsed time
        first = current    #  Move to the next position

    print(f"Couldn't find {item} in the list")    #  Couldn't find the item in the list
    return None

            # ---------------- Debuging Information  ----------------------
# Get user input for list size and search item
list_size = int(input('Enter the size of the list: '))
search_item = int(input('Enter the number to search for: '))

# Create a list to perform searches
my_list = [i for i in range(list_size)]

# Measure time and steps for binary search
start_time = time.perf_counter()
binary_steps, binary_end_time = binary_search(my_list, search_item)
binary_total_time = round(binary_end_time - start_time, 4)

# Measure time and steps for simple search
start_time = time.perf_counter()
simple_steps, simple_end_time = simple_search(my_list, search_item)
simple_total_time = round(simple_end_time - start_time, 4)

# Display the results
print(f"\nBinary Search Result: Found number {search_item} in {binary_steps} steps and {binary_total_time} seconds")
print(f"Simple Search Result: Found  number {search_item} in {simple_steps} steps and {simple_total_time} seconds")
