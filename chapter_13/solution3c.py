def max(array):
    if not array:
        return None

    greatest_number_so_far = array[0]

    for number in array:
        if number > greatest_number_so_far:
            greatest_number_so_far = number

    return greatest_number_so_far
