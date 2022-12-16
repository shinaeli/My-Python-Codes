def find_smallest(arr):
    # Assume the first item in the array is the smallest
    smallest = arr[0]
    # Therefore, smallest_index is automatically 0
    smallest_index = 0

    # Looping through the items in the array starting from the second item
    for i in range(1, len(arr)):

        # Check if the item in the current iteration is lower tha the initially assigned 'smallest' variable
        if arr[i] < smallest:
            # If the above condition is true, re-assign the 'smallest' variable to the item in the current iteration
            smallest = arr[i]
            # Also, re-assign the 'smallest_index' to the index of the item in the current iteration
            smallest_index = i

    # Return the 'smallest_index' found
    return smallest_index


# print(find_smallest([5, 3, 6, 2, 10]))


def selection_sort(arr):
    # Create an empty array called 'newArr'
    newArr = []

    # Looping through the provided array
    for i in range(len(arr)):
        # In each iteration, call the 'find_smallest' function on the provided array
        # Assign the value returned to the variable 'smallest'
        smallest = find_smallest(arr)
        # Use 'smallest' as an index to remove the item in the provided array
        # The removed item is appended to the array 'newArr'
        newArr.append(arr.pop(smallest))

    return newArr


print(selection_sort([5, 3, 6, 2, 10])) #[2, 3, 5, 6, 10]
print(selection_sort([29, 10, 6, 18, -6, 48, -21, -405, 3, 15])) #[-405, -21, -6, 3, 6, 10, 15, 18, 29, 48]

