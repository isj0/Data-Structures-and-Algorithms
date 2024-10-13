def max(array):
    if not array:
        return None

    for i in array:
        i_is_greatest_number = True

        for j in array:
            if j > i:
                i_is_greatest_number = False

        if i_is_greatest_number:
            return i
