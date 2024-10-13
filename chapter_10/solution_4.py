def print_all_items(array):
    for value in array:
        # If the current value is a Python "list", in other words, an array:
        if isinstance(value, list):
            print_all_items(value)
        else:
            print(value)
