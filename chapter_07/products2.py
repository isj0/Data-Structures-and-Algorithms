def two_number_products(array1, array2):
    products = []

    for i in array1:
        for j in array2:
            products.append(i * j)

    return products
