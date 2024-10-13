def average_celsius(fahrenheit_readings):
    if not fahrenheit_readings:
        return None

    celsius_numbers = []

    # Convert each reading to Celsius and append to array:
    for fahrenheit_reading in fahrenheit_readings:
        celsius_conversion = (fahrenheit_reading - 32) / 1.8
        celsius_numbers.append(celsius_conversion)

    # Calculate average:
    sum = 0

    for celsius_number in celsius_numbers:
        sum += celsius_number

    return sum // len(celsius_numbers)
