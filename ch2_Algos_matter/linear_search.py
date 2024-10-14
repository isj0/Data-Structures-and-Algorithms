# Implementation of linear search in an ordered array

def linear_search(array, search_value):

    for index, element in enumerate(array):

        if element == search_value:
            return index
        elif element > search_value:
            break
    
    return None

print(linear_search([3, 17, 75, 80, 202], 22))
print(linear_search([3, 17, 75, 80, 202], 80))