def sum(array):
    # Base case: an empty array
    if not array:
        return 0

    return array[0] + sum(array[1:])
