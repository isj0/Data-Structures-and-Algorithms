def find_missing_number(array):
    full_sum = 0

    for num in range(1, len(array) + 1):
        full_sum += num

    current_sum = 0

    for num in array:
        current_sum += num

    return full_sum - current_sum
