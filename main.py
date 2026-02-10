import sys
import os
import time


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Pre-populated data
library_books = [
    {
        'id': 'B001',
        'title': 'Python Programming',
        'author': 'John Smith',
        'total_stock': 5,
        'available_stock': 5,
        'borrowed_by': []
    },
    {
        'id': 'B002',
        'title': 'Data Structures',
        'author': 'Jane Doe',
        'total_stock': 3,
        'available_stock': 3,
        'borrowed_by': []
    },
    {
        'id': 'B003',
        'title': 'Web Development',
        'author': 'Mike Johnson',
        'total_stock': 4,
        'available_stock': 4,
        'borrowed_by': []
    },
    {
        'id': 'B004',
        'title': 'Database Systems',
        'author': 'Sarah Williams',
        'total_stock': 6,
        'available_stock': 6,
        'borrowed_by': []
    },
    {
        'id': 'B005',
        'title': 'Machine Learning',
        'author': 'David Brown',
        'total_stock': 2,
        'available_stock': 2,
        'borrowed_by': []
    },
    {
        'id': 'B006',
        'title': 'Algorithms',
        'author': 'Emma Davis',
        'total_stock': 4,
        'available_stock': 4,
        'borrowed_by': []
    },
    {
        'id': 'B007',
        'title': 'Computer Networks',
        'author': 'Tom Wilson',
        'total_stock': 3,
        'available_stock': 3,
        'borrowed_by': []
    },
    {
        'id': 'B008',
        'title': 'Operating Systems',
        'author': 'Lisa Anderson',
        'total_stock': 5,
        'available_stock': 5,
        'borrowed_by': []
    }
]

users = [
    {
        'username': 'admin',
        'password': 'admin123',
        'role': 'admin',
        'borrowed_books': []
    },
    {
        'username': 'student1',
        'password': 'pass123',
        'role': 'student',
        'borrowed_books': []
    },
    {
        'username': 'student2',
        'password': 'pass123',
        'role': 'student',
        'borrowed_books': []
    },
    {
        'username': 'student3',
        'password': 'pass123',
        'role': 'student',
        'borrowed_books': []
    }
]

current_user = None
next_book_id = 9


def login():
    global current_user
    print("\n=== Login to Library System ===")
    print("Default accounts:")
    print("Admin - username: admin, password: admin123")
    print("Student - username: student1, password: pass123")
    print("Student - username: student2, password: pass123")
    print("Student - username: student3, password: pass123\n")
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            current_user = user
            input(f"\nLogin successful! Welcome {username} ({user['role']}). (Press enter to continue)")
            return True
    
    input("Login failed! Invalid username or password. (Press enter to continue)")
    return False


# ========== ADMIN FUNCTIONS ==========

def add_book():
    global next_book_id
    print("\n--- Add New Book ---")
    t = input("Enter book title: ").strip()
    a = input("Enter author name: ").strip()
    
    try:
        stock = int(input("Enter total stock quantity: ").strip())
        
        if stock < 1:
            input("Error: Stock must be at least 1. (Press enter to continue)")
            return
    except ValueError:
        input("Error: Please enter a valid number for stock. (Press enter to continue)")
        return
    
    if len(t) > 0 and len(a) > 0:
        book_id = f'B{next_book_id:03d}'
        next_book_id += 1
        
        book = {
            'id': book_id,
            'title': t,
            'author': a,
            'total_stock': stock,
            'available_stock': stock,
            'borrowed_by': []
        }
        library_books.append(book)
        input(f"Success: Book added with ID {book_id}. (Press enter to continue)")
    else:
        input("Error: Title and Author cannot be empty. (Press enter to continue)")


def delete_book():
    print("\n--- Delete Book ---")
    
    if not library_books:
        input("Library is empty. (Press enter to continue)")
        return
    
    for i, book in enumerate(library_books, start=1):
        print(f"{i}. ID: {book['id']} | {book['title'].title()} | {book['author'].title()} | Stock: {book['available_stock']}/{book['total_stock']}")
    
    try:
        pos = int(input("\nEnter book number to delete: "))
        
        if pos < 1 or pos > len(library_books):
            input("Invalid position. (Press enter to continue)")
            return
        
        book = library_books[pos - 1]
        
        if len(book['borrowed_by']) > 0:
            input(f"Cannot delete! {len(book['borrowed_by'])} copies are currently borrowed. (Press enter to continue)")
            return
        
        confirm = input(f"Are you sure you want to delete '{book['title'].title()}'? (y/n): ").strip().lower()
        
        if confirm == 'y':
            library_books.pop(pos - 1)
            input("Success: Book deleted. (Press enter to continue)")
        else:
            input("Delete cancelled. (Press enter to continue)")
    
    except ValueError:
        input("Error: Please enter a valid number. (Press enter to continue)")


def edit_book():
    print("\n--- Edit Book ---")
    
    if not library_books:
        input("Library is empty. (Press enter to continue)")
        return
    
    for i, book in enumerate(library_books, start=1):
        print(f"{i}. ID: {book['id']} | {book['title'].title()} | {book['author'].title()}")
    
    try:
        pos = int(input("\nEnter book number to edit: "))
        
        if pos < 1 or pos > len(library_books):
            input("Invalid position. (Press enter to continue)")
            return
        
        book = library_books[pos - 1]
        
        print("\nLeave blank to keep current value")
        new_title = input(f"New title [{book['title']}]: ").strip()
        new_author = input(f"New author [{book['author']}]: ").strip()
        new_stock = input(f"New total stock [{book['total_stock']}]: ").strip()
        
        if new_title:
            book['title'] = new_title
        if new_author:
            book['author'] = new_author
        if new_stock:
            try:
                stock_num = int(new_stock)
                borrowed_count = len(book['borrowed_by'])
                if stock_num >= borrowed_count:
                    book['total_stock'] = stock_num
                    book['available_stock'] = stock_num - borrowed_count
                else:
                    input(f"Error: Cannot set stock below borrowed count ({borrowed_count}). (Press enter to continue)")
                    return
            except ValueError:
                input("Error: Invalid stock number. (Press enter to continue)")
                return
        
        input("Success: Book updated. (Press enter to continue)")
    
    except ValueError:
        input("Error: Please enter a valid number. (Press enter to continue)")


def view_all_users():
    print("\n--- All Users ---")
    
    for i, user in enumerate(users, start=1):
        borrowed_count = len(user['borrowed_books'])
        print(f"{i}. Username: {user['username']} | Role: {user['role']} | Books borrowed: {borrowed_count}")
        
        if borrowed_count > 0:
            print(f"   Borrowed book IDs: {', '.join(user['borrowed_books'])}")
    
    input("\n(Press enter to continue)")


def view_book_status():
    print("\n--- Book Status Report ---")
    
    if not library_books:
        input("No books available. (Press enter to continue)")
        return
    
    total_books = 0
    total_available = 0
    total_borrowed = 0
    
    for book in library_books:
        total_books += book['total_stock']
        total_available += book['available_stock']
        borrowed = book['total_stock'] - book['available_stock']
        total_borrowed += borrowed
        
        status = "Available" if book['available_stock'] > 0 else "All Borrowed"
        
        print(f"\nID: {book['id']}")
        print(f"Title: {book['title'].title()}")
        print(f"Author: {book['author'].title()}")
        print(f"Stock: {book['available_stock']}/{book['total_stock']} available")
        print(f"Status: {status}")
        
        if len(book['borrowed_by']) > 0:
            print(f"Borrowed by: {', '.join(book['borrowed_by'])}")
    
    print(f"\n--- Summary ---")
    print(f"Total books in library: {total_books}")
    print(f"Available: {total_available}")
    print(f"Borrowed: {total_borrowed}")
    
    input("\n(Press enter to continue)")


# ========== STUDENT FUNCTIONS ==========

def search_books():
    print("\n--- Search Books ---")
    query = input("Enter search term: ")
    
    query_clean = query.strip()
    query_lower = query_clean.lower()
    
    found_books = []
    
    for book in library_books:
        title_match = book['title'].lower().find(query_lower)
        author_match = book['author'].lower().find(query_lower)
        id_match = book['id'].lower().find(query_lower)
        
        if title_match != -1 or author_match != -1 or id_match != -1:
            found_books.append(book)
    
    if found_books:
        print(f"\nFound {len(found_books)} result(s) for '{query_clean}':")
        for book in found_books:
            status = "Available" if book['available_stock'] > 0 else "All Borrowed"
            print(f"ID: {book['id']} | Title: {book['title'].title()} | Author: {book['author'].title()} | Stock: {book['available_stock']}/{book['total_stock']} | {status}")
    else:
        print(f"No books found matching '{query_clean}'")
    
    input("(Press enter to continue)")


def display_all():
    print(f"\n--- All Books ({len(library_books)}) ---")
    
    if not library_books:
        input("No books available. (Press enter to continue)")
        return
    
    for i, book in enumerate(library_books, start=1):
        status = "Available" if book['available_stock'] > 0 else "All Borrowed"
        print(f"{i}. ID: {book['id']} | Title: {book['title'].title()} | Author: {book['author'].title()} | Stock: {book['available_stock']}/{book['total_stock']} | {status}")
    
    input("(Press enter to continue)")


def borrow_book():
    print("\n--- Borrow Book ---")
    
    if not library_books:
        input("No books available. (Press enter to continue)")
        return
    
    # Show available books
    available_books = [book for book in library_books if book['available_stock'] > 0]
    
    if not available_books:
        input("No books are currently available for borrowing. (Press enter to continue)")
        return
    
    print("Available books:")
    for i, book in enumerate(available_books, start=1):
        print(f"{i}. ID: {book['id']} | {book['title'].title()} | {book['author'].title()} | Available: {book['available_stock']}")
    
    try:
        choice = int(input("\nEnter book number to borrow: "))
        
        if choice < 1 or choice > len(available_books):
            input("Invalid choice. (Press enter to continue)")
            return
        
        book = available_books[choice - 1]
        
        # Check if user already borrowed this book
        if book['id'] in current_user['borrowed_books']:
            input("You have already borrowed this book. (Press enter to continue)")
            return
        
        # Borrow the book
        book['available_stock'] -= 1
        book['borrowed_by'].append(current_user['username'])
        current_user['borrowed_books'].append(book['id'])
        
        input(f"Success! You have borrowed '{book['title'].title()}'. (Press enter to continue)")
    
    except ValueError:
        input("Error: Please enter a valid number. (Press enter to continue)")


def return_book():
    print("\n--- Return Book ---")
    
    if not current_user['borrowed_books']:
        input("You have not borrowed any books. (Press enter to continue)")
        return
    
    print("Your borrowed books:")
    borrowed_books_list = []
    
    for book_id in current_user['borrowed_books']:
        for book in library_books:
            if book['id'] == book_id:
                borrowed_books_list.append(book)
                break
    
    for i, book in enumerate(borrowed_books_list, start=1):
        print(f"{i}. ID: {book['id']} | {book['title'].title()} | {book['author'].title()}")
    
    try:
        choice = int(input("\nEnter book number to return: "))
        
        if choice < 1 or choice > len(borrowed_books_list):
            input("Invalid choice. (Press enter to continue)")
            return
        
        book = borrowed_books_list[choice - 1]
        
        # Return the book
        book['available_stock'] += 1
        book['borrowed_by'].remove(current_user['username'])
        current_user['borrowed_books'].remove(book['id'])
        
        input(f"Success! You have returned '{book['title'].title()}'. (Press enter to continue)")
    
    except ValueError:
        input("Error: Please enter a valid number. (Press enter to continue)")


def view_my_books():
    print("\n--- My Borrowed Books ---")
    
    if not current_user['borrowed_books']:
        input("You have not borrowed any books. (Press enter to continue)")
        return
    
    print(f"You have borrowed {len(current_user['borrowed_books'])} book(s):\n")
    
    for book_id in current_user['borrowed_books']:
        for book in library_books:
            if book['id'] == book_id:
                print(f"ID: {book['id']} | Title: {book['title'].title()} | Author: {book['author'].title()}")
                break
    
    input("\n(Press enter to continue)")


# ========== MENU FUNCTIONS ==========

def admin_menu():
    while True:
        clear_screen()
        print(f"\n=== Library System - Admin ({current_user['username']}) ===")
        print("1. Add Book")
        print("2. Edit Book")
        print("3. Delete Book")
        print("4. Search Books")
        print("5. Display All Books")
        print("6. View Book Status")
        print("7. View All Users")
        print("8. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            edit_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '5':
            display_all()
        elif choice == '6':
            view_book_status()
        elif choice == '7':
            view_all_users()
        elif choice == '8':
            print("Logging out...")
            return
        else:
            input("Invalid choice. (Press enter to continue)")


def student_menu():
    while True:
        clear_screen()
        print(f"\n=== Library System - Student ({current_user['username']}) ===")
        print("1. Search Books")
        print("2. Display All Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View My Borrowed Books")
        print("6. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            search_books()
        elif choice == '2':
            display_all()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            view_my_books()
        elif choice == '6':
            print("Logging out...")
            return
        else:
            input("Invalid choice. (Press enter to continue)")


def main():
    global current_user
    
    while True:
        clear_screen()
        
        if current_user is None:
            if not login():
                continue
        
        if current_user['role'] == 'admin':
            admin_menu()
        else:
            student_menu()
        
        current_user = None


if __name__ == "__main__":
    main()