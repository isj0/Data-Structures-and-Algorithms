def find_needle(needle, haystack):
    needle_start_index = 0

    while needle_start_index <= len(haystack) - len(needle):
        if needle[0] == haystack[needle_start_index]:
            needle_offset = 0

            while needle_offset < len(needle):
                if (needle[needle_offset]
                        != haystack[needle_start_index + needle_offset]):
                    break
                else:
                    if needle_offset == len(needle) - 1:
                        return True

                needle_offset += 1

        needle_start_index += 1

    return False
