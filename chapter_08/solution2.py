def find_duplicate(array):
    hash_table = {}

    for value in array:
        if hash_table.get(value):
            return value
        else:
            hash_table[value] = True

    return None
