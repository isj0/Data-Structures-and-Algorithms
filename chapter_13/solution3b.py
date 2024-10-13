def max(array):
    if not array:
        return None

    array.sort()

    return array[-1]
