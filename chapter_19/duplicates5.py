def has_duplicate_value(array):
    existing_values = {}

    for value in array:
        if value not in existing_values:
            existing_values[value] = True
        else:
            return True

    return False
