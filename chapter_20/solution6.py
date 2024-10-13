def longest_sequence_length(array):
    hash_table = {}
    greatest_sequence_length = 0

    for number in array:
        hash_table[number] = True

    for number in array:
        if not hash_table.get(number - 1):
            current_sequence_length = 1
            current_number = number

            while hash_table.get(current_number + 1):
                current_number += 1
                current_sequence_length += 1

                if current_sequence_length > greatest_sequence_length:
                    greatest_sequence_length = current_sequence_length

    return greatest_sequence_length
