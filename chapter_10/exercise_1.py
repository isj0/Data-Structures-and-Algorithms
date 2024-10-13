def print_every_other(low, high):
    if low > high:
        return

    print(low)
    print_every_other(low + 2, high)
