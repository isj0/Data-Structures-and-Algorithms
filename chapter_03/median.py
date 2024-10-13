def median(array):
    if not array:
        return None

    middle = len(array) // 2

    # If array has even amount of numbers:
    if len(array) % 2 == 0:
        return (array[middle - 1] + array[middle]) / 2.0
    else:  # If array has odd amount of numbers:
        return array[middle]
