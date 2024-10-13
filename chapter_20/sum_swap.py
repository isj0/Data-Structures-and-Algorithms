def sum_swap(array_1, array_2):
    hash_table = {}
    sum_1 = 0
    sum_2 = 0

    for index, num in enumerate(array_1):
        sum_1 += num
        hash_table[num] = index

    for num in array_2:
        sum_2 += num

    # If the input consists of integers and the difference
    # between the two sums are odd, it's impossible to find
    # an integer smack in the middle, so no swap is possible:
    if (sum_1 - sum_2) % 2 == 1:
        return None

    shift_amount = (sum_1 - sum_2) // 2

    for index, num in enumerate(array_2):
        if num + shift_amount in hash_table:
            return [hash_table[num + shift_amount], index]

    return None
