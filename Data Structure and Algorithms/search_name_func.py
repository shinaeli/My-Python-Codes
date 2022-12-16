from students_record import students_register


def search_name(arr, item):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        guessed_number = arr[int(mid)]
        if guessed_number == item:
            show_name = students_register[int(mid)]['name']
            show_age = students_register[int(mid)]['age']
            return f'The student\'s name is {show_name}, aged {show_age} years.'
        elif guessed_number > item:
            high = mid - 1
        else:
            low = mid + 1
    return f'The student\'s record doesn\'t exist.'