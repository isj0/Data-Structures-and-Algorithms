def find_missing_number(array):
    for number in range(len(array) + 1):
        if number not in array:
            return number

    return None
