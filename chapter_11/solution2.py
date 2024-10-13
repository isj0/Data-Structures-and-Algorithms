def select_even(array):
    if not array:
        return []

    if array[0] % 2 == 0:
        return [array[0]] + select_even(array[1:])
    else:
        return select_even(array[1:])
