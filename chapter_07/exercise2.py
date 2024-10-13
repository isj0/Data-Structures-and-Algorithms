def merge(array_1, array_2):
    new_array = []
    array_1_pointer = 0
    array_2_pointer = 0

    # Run the loop until we've reached end of both arrays:
    while array_1_pointer < len(array_1) or array_2_pointer < len(array_2):

        # If we already reached the end of the first array,
        # add item from second array:
        if array_1_pointer >= len(array_1):
            new_array.append(array_2[array_2_pointer])
            array_2_pointer += 1
        # If we already reached the end of the second array,
        # add item from first array:
        elif array_2_pointer >= len(array_2):
            new_array.append(array_1[array_1_pointer])
            array_1_pointer += 1
        # If the current number in first array is less than current
        # number in second array, add from first array:
        elif array_1[array_1_pointer] < array_2[array_2_pointer]:
            new_array.append(array_1[array_1_pointer])
            array_1_pointer += 1
        # If the current number in second array is less than or equal
        # to current number in first array, add from second array:
        else:
            new_array.append(array_2[array_2_pointer])
            array_2_pointer += 1

    return new_array
