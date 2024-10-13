def max(array):
    if not array:
        return None

    if len(array) == 1:
        return array[0]

    if array[0] > max(array[1:]):
        return array[0]
    else:
        return max(array[1:])
