def max(array):
    if not array:
        return None

    if len(array) == 1:
        return array[0]

    # Calculate the max of the remainder of the array
    # and store it inside a variable:
    max_of_remainder = max(array[1:])

    # Comparison of first number against this variable:
    if array[0] > max_of_remainder:
        return array[0]
    else:
        return max_of_remainder
