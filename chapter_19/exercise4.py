def double_array_1(array):
    new_array = []

    for value in array:
        new_array.append(value * 2)

    return new_array


def double_array_2(array):
    for i in range(len(array)):
        array[i] *= 2

    return array


def double_array_3(array, index=0):
    if index >= len(array):
        return

    array[index] *= 2
    double_array_3(array, index + 1)

    return array
