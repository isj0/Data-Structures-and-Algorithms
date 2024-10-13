def find_missing_letter(string):
    hash_table = {}

    for char in string:
        hash_table[char] = True

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        if not hash_table.get(char):
            return char

    return None
