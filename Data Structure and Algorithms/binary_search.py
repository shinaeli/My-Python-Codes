def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        guessed_item = arr[int(mid)]
        if guessed_item == item:
            return int(mid)
        elif guessed_item > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search([3, 7, 12, 14, 19, 36, 40], 12)) #2
print(binary_search([3, 7, 12, 14, 19, 36, 40], 10)) #-1
print(binary_search([3, 7, 12, 14, 19, 36, 40], 40)) #6

