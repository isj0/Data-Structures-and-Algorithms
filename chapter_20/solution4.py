def greatest_product(array):
    greatest_number = float("-inf")
    second_to_greatest_number = float("-inf")

    lowest_number = float("inf")
    second_to_lowest_number = float("inf")

    for number in array:
        if number >= greatest_number:
            second_to_greatest_number = greatest_number
            greatest_number = number
        elif number > second_to_greatest_number:
            second_to_greatest_number = number

        if number <= lowest_number:
            second_to_lowest_number = lowest_number
            lowest_number = number
        elif number < second_to_lowest_number:
            second_to_lowest_number = number

    greatest_product_from_two_highest = (greatest_number
                                         * second_to_greatest_number)

    greatest_product_from_two_lowest = (lowest_number
                                        * second_to_lowest_number)

    if (greatest_product_from_two_highest
            > greatest_product_from_two_lowest):
        return greatest_product_from_two_highest
    else:
        return greatest_product_from_two_lowest
