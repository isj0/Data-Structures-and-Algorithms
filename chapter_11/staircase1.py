def number_of_paths(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return (number_of_paths(n - 1)
            + number_of_paths(n - 2)
            + number_of_paths(n - 3))
