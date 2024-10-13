def mark_inventory(clothing_items):
    clothing_options = []

    for item in clothing_items:
        for size in range(1, 6):
            clothing_options.append(item + " Size: " + str(size))

    return clothing_options
