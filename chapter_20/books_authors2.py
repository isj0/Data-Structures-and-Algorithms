def connect_books_with_authors(books, authors):
    books_with_authors = []
    author_hash_table = {}

    for author in authors:
        author_hash_table[author["author_id"]] = author["name"]

    for book in books:
        books_with_authors.append({"title": book["title"],
            "author": author_hash_table[book["author_id"]]})

    return books_with_authors
