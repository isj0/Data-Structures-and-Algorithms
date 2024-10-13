def select_a_strings(array):
    new_array = []

    for string in array:
        if string[0] == "a":
            new_array.append(string)

    return new_array
