def add_until_100(array):
    if not array:
        return 0

    sum_of_remaining_numbers = add_until_100(array[1:])

    if array[0] + sum_of_remaining_numbers > 100:
        return sum_of_remaining_numbers
    else:
        return array[0] + sum_of_remaining_numbers
