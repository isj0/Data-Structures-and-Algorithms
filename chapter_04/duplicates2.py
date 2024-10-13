def has_duplicate_value(array):
    steps = 0  # count of steps
    for i in range(len(array)):
        for j in range(len(array)):
            steps += 1  # increment number of steps
            if (i != j) and (array[i] == array[j]):
                return True

    print(steps)  # print number of steps if no duplicates
    return False
