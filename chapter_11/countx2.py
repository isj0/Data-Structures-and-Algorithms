def count_x(string):

    # Base case: an empty string
    if not string:
        return 0

    if string[0] == "x":
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])
