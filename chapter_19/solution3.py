def reverse(array):
    i = 0

    while i < len(array) // 2:
        mirror_of_i = len(array) - 1 - i
        array[i], array[mirror_of_i] = array[mirror_of_i], array[i]

        i += 1

    return array
