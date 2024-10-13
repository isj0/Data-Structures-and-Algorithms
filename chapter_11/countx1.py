def count_x(string):

    # Two base cases:
    if len(string) == 1:
        if string[0] == "x":
            return 1
        else:
            return 0

    if string[0] == "x":
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])
