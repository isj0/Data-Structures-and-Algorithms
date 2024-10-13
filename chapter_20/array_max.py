def max(array):
    if not array:
        return None

    greatest_number = array[0]

    for number in array:
        if number > greatest_number:
            greatest_number = number

    return greatest_number
