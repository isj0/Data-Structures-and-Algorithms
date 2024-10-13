def reverse(array):
    new_array = []

    for value in array:
        new_array.insert(0, value)

    return new_array
