def are_anagrams(first_string, second_string):
    second_string_array = list(second_string)

    for i in range(len(first_string)):
        if len(second_string_array) == 0:
            return False

        for j in range(len(second_string_array)):
            if first_string[i] == second_string_array[j]:
                del second_string_array[j]
                break

    return len(second_string_array) == 0
