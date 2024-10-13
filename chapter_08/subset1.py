def is_subset(array1, array2):

    # Determine which array is smaller:
    if len(array1) > len(array2):
        larger_array = array1
        smaller_array = array2
    else:
        larger_array = array2
        smaller_array = array1

    # Iterate through smaller array:
    for i in smaller_array:

        # Assume temporarily that the current value from
        # smaller array is not found in larger array:
        found_match = False

        # For each value in smaller array, iterate through
        # larger array:
        for j in larger_array:

            # If the two values are equal, it means the current
            # value in smaller array is present in the larger array:
            if i == j:
                found_match = True
                break

        # If the current value in smaller array doesn't exist
        # in larger array, return false:
        if not found_match:
            return False

    # If we get to the end of the loops, it means that all
    # values from smaller array are present in larger array:
    return True
