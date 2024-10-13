def has_duplicate_value(array):
    existing_numbers = [0] * 11

    for i in range(len(array)):
        if existing_numbers[array[i]] == 1:
            return True
        else:
            existing_numbers[array[i]] = 1

    return False
