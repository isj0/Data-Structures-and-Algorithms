def connect_books_with_authors(books, authors):
    books_with_authors = []

    for book in books:
        for author in authors:
            if book["author_id"] == author["author_id"]:
                books_with_authors.append({"title": book["title"], 
                                           "author": author["name"]})

    return books_with_authors
