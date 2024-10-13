def has_duplicate_value(array):
    array.sort()

    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            return True

    return False
