def word_builder(array):
    collection = []

    for index_i, i in enumerate(array):
        for index_j, j in enumerate(array):
            for index_k, k in enumerate(array):
                if (index_i != index_j and
                        index_j != index_k and index_i != index_k):
                    collection.append(i + j + k)

    return collection
