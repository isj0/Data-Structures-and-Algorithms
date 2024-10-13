def greatest_number(array):
    if not array:
        return None

    greatest_number_so_far = array[0]

    for i in array:
        if i > greatest_number_so_far:
            greatest_number_so_far = i

    return greatest_number_so_far
