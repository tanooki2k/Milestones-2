"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name,author,read  (comma separated)
"""
import csv

books_file = "/home/javier/PycharmProjects/milestones/data.txt"
fieldnames = ["name", "author", "read"]


def add_book(name, author):
    item = {"name": name, "author": author, "read": 0}

    with open(books_file, "a") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writerow(item)


def get_all_books():
    with open(books_file) as file:
        csv_reader = csv.DictReader(file)
        lines = [row for row in csv_reader]
    return lines


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 1
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, "w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(books)


def create_book_table():
    with open(books_file, "a") as file:
        if file.tell() == 0:
            csv.DictWriter(file, fieldnames=fieldnames).writeheader()


if __name__ == "__main__":
    pass
