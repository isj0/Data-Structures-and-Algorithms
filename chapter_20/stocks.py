def is_increasing_triplet(array):
    lowest_price = array[0]
    middle_price = float('inf')

    for price in array:
        if price <= lowest_price:
            lowest_price = price
        elif price <= middle_price:
            middle_price = price
        else:
            return True

    return False
