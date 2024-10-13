def sort_temperatures(array):
    hash_table = {}

    for temperature in array:
        if temperature in hash_table:
            hash_table[temperature] += 1
        else:
            hash_table[temperature] = 1

    sorted_temperatures = []
    temperature = 95

    while temperature <= 105:
        if temperature in hash_table:
            for i in range(hash_table[temperature]):
                sorted_temperatures.append(temperature)

        temperature += 1

    return sorted_temperatures
