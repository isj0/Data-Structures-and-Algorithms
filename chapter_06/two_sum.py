def two_sum(array):
    for index_i, i in enumerate(array):
        for index_j, j in enumerate(array):
            if (index_i != index_j) and (i + j == 10):
                return True

    return False
