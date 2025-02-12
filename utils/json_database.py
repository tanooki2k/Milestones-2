"""
Handles the storage and retrieval of books using a JSON file.
Note: JSON can store various types of data.
Structure of the JSON file:

[
    {
        "name": "Book Title",
        "author": "Author Name",
        "read": true
    }
]

Each book is represented as a dictionary with the following fields:
- "name": The title of the book (string)
- "author": The author's name (string)
- "read": The read status of the book (boolean, where true indicates the book has been read)
"""
import json

books_file = "/home/javier/PycharmProjects/milestones/data.json"


def add_book(name, author):
    books = get_all_books()
    item = {"name": name, "author": author, "read": False}
    books.append(item)
    _save_all_books(books)


def get_all_books():
    with open(books_file) as file:
        return json.load(file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, "w") as file:
        json.dump(books, file, indent=4)


def create_book_table():
    with open(books_file, "a") as file:
        if file.tell() == 0:
            json.dump([], file, indent=4)


if __name__ == "__main__":
    pass
