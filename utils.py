def find_max(lists):
    max_item = lists[0]
    for item in  lists:
        if item > max_item:
            max_item = item
    return max_item