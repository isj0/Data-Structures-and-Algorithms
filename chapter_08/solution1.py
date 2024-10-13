def get_intersection(array1, array2):
    intersection = []
    hash_table = {}

    for value in array1:
        hash_table[value] = True

    for value in array2:
        if hash_table.get(value):
            intersection.append(value)

    return intersection
