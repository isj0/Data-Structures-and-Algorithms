def one_hundred_sum(array):
    if (len(array) % 2 != 0) or not array:
        return False

    left_index = 0
    right_index = len(array) - 1

    while left_index < (len(array) // 2):
        if array[left_index] + array[right_index] != 100:
            return False

        left_index += 1
        right_index -= 1

    return True
