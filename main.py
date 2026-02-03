import sys
import os
import time


def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        os.system('cls')
    else:
        # Command for Linux/macOS/Posix
        os.system('clear')


library_books = []


def add_book():
    print("\n--- Add New Book ---")
    t = input("Enter book title: ").strip()
    a = input("Enter author name: ").strip()

    if len(t) > 0 and len(a) > 0:
        book = {
            'title': t,
            'author': a,
            'status': 'Available'
        }
        library_books.append(book)
        input("Success: Book added. (Press enter to continue)")
    else:
        input("Error: Title and Author cannot be empty. (Press enter to continue)")


def search_books():
    print("\n--- Search Books ---")
    query = input("Enter search term: ")

    query_clean = query.strip()
    query_lower = query_clean.lower()

    found_books = []

    for book in library_books:
        title_match = book['title'].lower().find(query_lower)
        author_match = book['author'].lower().find(query_lower)

        if title_match != -1 or author_match != -1:
            found_books.append(book)

    if found_books:
        print(f"\nFound {len(found_books)} result(s) for '{query_clean}':")
        for book in found_books:
            print(
                f"Title: {book['title'].title()} | Author: {book['author'].title()}"
            )
    else:
        print(f"No books found matching '{query_clean}'")

    input("(Press enter to continue)")


def display_all():
    print(f"\n--- All Books ({len(library_books)}) ---")

    if not library_books:
        input("No books available. (Press enter to continue)")
        return

    for i, book in enumerate(library_books, start=1):
        print(
            f"{i}. Title: {book['title'].title()} | Author: {book['author'].title()}"
        )
    input("(Press enter to continue)")


def delete_book():
    print("\n--- Delete Book (By Position) ---")

    if not library_books:
        input("Library is empty. (Press enter to continue)")
        return

    for i, book in enumerate(library_books, start=1):
        print(f"{i}. {book['title'].title()} | {book['author'].title()}")

    try:
        pos = int(input("\nEnter book number to delete :"))

        if pos < 1 or pos > len(library_books):
            input("Invalid position. (Press enter to continue)")
            return

        book = library_books[pos - 1]

        confirm = input(
            f"Are you sure you want to delete '{book['title'].title()}'? (y/n): "
        ).strip().lower()

        if confirm == 'y':
            library_books.pop(pos - 1)
            input("Success: Book deleted. (Press enter to continue)")
        else:
            input("Delete cancelled. (Press enter to continue)")

    except ValueError:
        input("Error: Please enter a valid number. (Press enter to continue)")


def edit_book():
    print("\n--- Edit Book (By Position) ---")

    if not library_books:
        input("Library is empty. (Press enter to continue)")
        return

    for i, book in enumerate(library_books, start=1):
        print(f"{i}. {book['title'].title()} | {book['author'].title()}")

    try:
        pos = int(input("\nEnter book number to edit: "))

        if pos < 1 or pos > len(library_books):
            input("Invalid position. (Press enter to continue)")
            return

        book = library_books[pos - 1]

        print("\nLeave blank to keep current value")
        new_title = input(f"New title [{book['title']}]: ").strip()
        new_author = input(f"New author [{book['author']}]: ").strip()

        if new_title:
            book['title'] = new_title
        if new_author:
            book['author'] = new_author

        input("Success: Book updated. (Press enter to continue)")

    except ValueError:
        input("Error: Please enter a valid number. (Press enter to continue)")


def main():
    while True:
        clear_screen()
        print("\n=== Library System ===")
        print("1. Add Book")
        print("2. Search Books")
        print("3. Display All")
        print("4. Delete Book")
        print("5. Edit Book")
        print("6: Exit")
        choice = input("Enter choice: ")

        match choice:
            case '1':
                add_book()
            case '2':
                search_books()
            case '3':
                display_all()
            case '4':
                delete_book()
            case '5':
                edit_book()
            case '6':
                print("Exiting...")
                break
            case _:
                input("Invalid choice. (Press enter to continue)")


if __name__ == "__main__":
    main()