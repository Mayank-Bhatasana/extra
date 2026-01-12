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
    # Week 3 Requirement: Use strip() to remove whitespace [cite: 31, 92]
    t = input("Enter book title: ").strip()
    a = input("Enter author name: ").strip()
    
    # Week 3 Requirement: Use title() to format names (e.g. "harry" -> "Harry") [cite: 33, 92]
    # We store it cleaned, but we can also format it during display.
    if len(t) > 0 and len(a) > 0:
        book = {
            'title': t,    # Storing raw input, will format on display
            'author': a,
            'status': 'Available'
        }
        library_books.append(book)
        input(f"Success: Book added. (Press enter to continue) ")
    else:
        input("Error: Title and Author cannot be empty. (Press enter to continue)")

def search_books():
    print("\n--- Search Books (Week 3 Feature) ---")
    query = input("Enter search term: ")

    # Week 3 Requirement: Use replace() to clean strings 
    # Example: Removing extra spaces user might have typed accidently
    query_clean = query.replace("  ", " ").strip()
    
    # Week 3 Requirement: Case-insensitive search using lower() [cite: 33, 92]
    query_lower = query_clean.lower()
    
    found_books = []
    
    for book in library_books:
        # Week 3 Requirement: Use find() for flexible search 
        # .find() returns the index of the string, or -1 if not found.
        title_match = book['title'].lower().find(query_lower)
        author_match = book['author'].lower().find(query_lower)
        
        if title_match != -1 or author_match != -1:
            found_books.append(book)
    
    # Display Results
    if found_books:
        print(f"\nFound {len(found_books)} result(s) for '{query_clean}':")
        for book in found_books:
            # Week 3 Requirement: Format output using .title() 
            print(f"Title: {book['title'].title()} | Author: {book['author'].title()}")
            input('(Press enter to continue)')
    else:
        print(f"No books found matching '{query_clean}'.")
        input('(Press enter to continue)')

def display_all():
    # Simple display to verify data
    print(f"\n--- All Books ({len(library_books)}) ---")
    for book in library_books:
        print(f"Title: {book['title'].title()} | Author: {book['author'].title()}")
        input('(Press enter to continue)')

# --- Main Menu (Week 2 Requirement) ---
def main():
    while True:
        clear_screen()
        print("\n=== Library System (Week 3 Build) ===")
        print("1. Add Book")
        print("2. Search Books (Week 3 Focus)")
        print("3. Display All")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            search_books()
        elif choice == '3':
            display_all()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
