def greatest_number(array):
    if not array:
        return None

    for i in array:
        # Assume for now that i is the greatest:
        is_i_the_greatest = True

        for j in array:
            # If we find another value that is greater than i,
            # i is not the greatest:
            if j > i:
                is_i_the_greatest = False

        # If, by the time we checked all the other numbers, i
        # is still the greatest, it means that i is the greatest number:
        if is_i_the_greatest:
            return i
