def first_non_duplicate(string):
    hash_table = {}

    for char in string:
        if hash_table.get(char):
            hash_table[char] += 1
        else:
            hash_table[char] = 1

    for char in string:
        if hash_table.get(char) == 1:
            return char

    return None
