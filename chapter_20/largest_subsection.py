def max_sum(array):
    current_sum = 0
    greatest_sum = 0

    for num in array:
        if current_sum + num < 0:
            current_sum = 0
        else:
            current_sum += num
            if current_sum > greatest_sum:
                greatest_sum = current_sum 

    return greatest_sum
