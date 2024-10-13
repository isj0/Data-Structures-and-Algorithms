def chessboard_space(number_of_grains):
    chessboard_spaces = 1
    placed_grains = 1

    while placed_grains < number_of_grains:
        placed_grains *= 2
        chessboard_spaces += 1

    return chessboard_spaces
