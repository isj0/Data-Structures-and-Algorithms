def word_builder(array):
    collection = []

    for index_i, i in enumerate(array):
        for index_j, j in enumerate(array):
            if index_i != index_j:
                collection.append(i + j)

    return collection
