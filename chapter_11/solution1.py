def character_count(array):
    # Base case: when the array is empty:
    if not array:
        return 0

    return len(array[0]) + character_count(array[1:])
