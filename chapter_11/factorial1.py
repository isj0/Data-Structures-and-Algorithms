def factorial(n):
    product = 1

    for num in range(1, n + 1):
        product *= num

    return product
