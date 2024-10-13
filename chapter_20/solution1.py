def find_multisport_athletes(array_1, array_2):
    hash_table = {}
    multisport_athletes = []

    for athlete in array_1:
        hash_table[athlete["first_name"]
                   + " "
                   + athlete["last_name"]] = True

    for athlete in array_2:
        if hash_table.get(athlete["first_name"]
                          + " "
                          + athlete["last_name"]):
            multisport_athletes.append(athlete["first_name"]
                                       + " "
                                       + athlete["last_name"])

    return multisport_athletes
