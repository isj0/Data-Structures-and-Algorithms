def average_of_even_numbers(array):
    sum = 0
    count_of_even_numbers = 0

    for number in array:
        if number % 2 == 0:
            sum += number
            count_of_even_numbers += 1

    if count_of_even_numbers == 0:
        return None

    return sum // count_of_even_numbers
