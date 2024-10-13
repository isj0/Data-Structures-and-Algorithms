def two_number_products(array):
    products = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            products.append(array[i] * array[j])

    return products
