def greatest_product(array):
    if len(array) < 2:
        return None

    greatest_product_so_far = array[0] * array[1]

    for index_i, value_i in enumerate(array):
        for index_j, value_j in enumerate(array):
            if (index_i != index_j and
                    value_i * value_j > greatest_product_so_far):
                greatest_product_so_far = value_i * value_j

    return greatest_product_so_far
