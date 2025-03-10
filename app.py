# from utils.csv_database import *
# from utils.json_database import *
from utils.database import *


def menu():
    create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        print()
        try:
            selected_function = options[user_input]
            selected_function()
        except KeyError:
            print('Unknown command. Please try again.')
        except TypeError:
            print('Function not implemented yet.')
        print()
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter the book name: ")
    author = input("Enter the book author: ")

    add_book(name, author)


def list_books():
    books = get_all_books()
    print("Books:" if books else "No books found.")
    for book in books:
        read = "YES" if str(book['read']) == "1" or book['read'] is True else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input("Enter the book name: ")

    mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the book name: ")

    delete_book(name)


choices = [
    ('a', 'to add a new book', prompt_add_book),
    ('l', 'to list all books', list_books),
    ('r', 'to mark a book as read', prompt_read_book),
    ('d', 'to delete a book', prompt_delete_book),
    ('q', 'to quit', None)
]

USER_CHOICE = "Enter:\n" + "\n".join(
    f"- '{key}' {description}" for key, description, _ in choices) + "\n\nYour choice: "

options = {
    item[0]: item[2] for item in choices
}

if __name__ == '__main__':
    menu()
