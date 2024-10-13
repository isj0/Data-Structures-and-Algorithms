def find_missing_number(array):
    array.sort()

    for index, num in enumerate(array):
        if num != index:
            return index

    return None
