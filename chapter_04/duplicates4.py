def has_duplicate_value(array):
    steps = 0
    existing_numbers = [0] * 11

    for i in range(len(array)):
        steps += 1
        if existing_numbers[array[i]] == 1:
            return True
        else:
            existing_numbers[array[i]] = 1

    print(steps)
    return False
