def is_palindrome(string):

    left_index = 0
    right_index = len(string) - 1

    # Iterate until left_index reaches the middle of the array:
    while left_index < len(string) // 2:

        # If the character on the left doesn't equal the character
        # on the right, the string is not a palindrome:
        if (string[left_index] != string[right_index]):
            return False

        left_index += 1
        right_index -= 1

    # If we got through the entire loop without finding any
    # mismatches, the string must be a palindrome:
    return True
