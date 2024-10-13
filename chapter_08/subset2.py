def is_subset(array1, array2):
    hash_table = {}

    # Determine which array is smaller:
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1

    for value in larger_array:
        hash_table[value] = True



    for value in smaller_array:
        if not hash_table.get(value):
            return False

    return True
