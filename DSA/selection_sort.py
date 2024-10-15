# Code Implmentation of Selection Sort

def selection_sort(array):
    for i in range(len(array) - 1):
        lowest_number_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j
        
        if lowest_number_index != i:
            array[i], array[lowest_number_index] = array[lowest_number_index], array[i]

    return array


print(selection_sort([7, 5, 4, 3, 1]))
