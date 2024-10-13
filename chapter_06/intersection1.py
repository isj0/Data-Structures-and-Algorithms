def intersection(first_array, second_array):
    result = []

    for i in first_array:
        for j in second_array:
            if i == j:
                result.append(i)

    return result
