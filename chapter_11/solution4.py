def index_of_x(string):
    if string[0] == "x":
        return 0

    return index_of_x(string[1:]) + 1
