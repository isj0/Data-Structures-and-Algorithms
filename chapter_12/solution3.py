def unique_paths(rows, columns, memo):

    if rows == 1 or columns == 1:
        return 1

    if (rows, columns) not in memo:
        memo[(rows, columns)] = (unique_paths(rows - 1, columns, memo)
                                 + unique_paths(rows, columns - 1, memo))

    return memo[(rows, columns)]
