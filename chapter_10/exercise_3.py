def sum(low, high):
    return high + sum(low, high - 1)
