from utils import *

books = {
    "1984": {"author": "Orwell", "available": True},
    "Dracula": {"author": "Stoker", "available": True},
    "Brave New World": {"author": "Huxley", "available": True},
    "Fahrenheit 451": {"author": "Bradbury", "available": True},
    "The Hobbit": {"author": "Tolkien", "available": True},
    "Moby Dick": {"author": "Melville", "available": True},
    "The Great Gatsby": {"author": "Fitzgerald", "available": True},
    "To Kill a Mockingbird": {"author": "Lee", "available": True},
    "War and Peace": {"author": "Tolstoy", "available": True},
    "Crime and Punishment": {"author": "Dostoevsky", "available": True}
}

borrowed_books = {}

def view_books():
    print_with_clear("\033[1;31mLibrary Catalog\033[0m")
    print()
    if not books:
        print("No books available.")
        return
    for title, info in books.items():
        status = "Available" if info["available"] else "Borrowed"
        print(f"{title} by {info['author']} - {status}")
    print()

def borrow_book():
    print_with_clear("\033[1;31mBorrow Book\033[0m")

    title = choose_option('Borrow Book', [title for title in books], 'Enter book to borrow: ')

    if title not in books:
        print(f"Book '{title}' not found in catalog.")
        return
    if not books[title]["available"]:
        print(f"Book '{title}' is currently not available.")
        return
    books[title]["available"] = False
    borrowed_books[title] = books[title]
    print(f"Book '{title}' borrowed successfully.")

def return_book():
    print_with_clear("\033[1;31mReturn Book\033[0m")
    if not borrowed_books:
        print("No books currently borrowed.")
        return
    
    title = choose_option('Return Book', [title for title in borrowed_books], 'Enter book to return: ')

    if title not in borrowed_books:
        print(f"Book '{title}' is not in borrowed list.")
        return
    
    books[title]["available"] = True
    del borrowed_books[title]
    print(f"Book '{title}' returned successfully.")

def add_book():
    print_with_clear("\033[1;31mAdd New Book\033[0m")
    title = input("Enter book title: ")
    if title in books:
        print(f"Book '{title}' already exists.")
        return
    author = input("Enter author name: ")
    books[title] = {"author": author, "available": True}
    print(f"Added book '{title}' by {author}.")

def view_borrowed_books():
    print_with_clear("\033[1;31mBorrowed Books\033[0m")

    print()
    if not borrowed_books:
        print("No books currently borrowed.")
        return
    for title, book in borrowed_books.items():
        print(f"{title} by {book['author']}")
    print()

while True:
    option = choose_option("Library Assistant", ["View All Books", "Borrow a Book", "Return a Book", "Add a New Book", "View Borrowed Books", "Exit"], "Choose an option: ")

    if option == "View All Books":
        view_books()
        input("Press Enter to continue...")
    elif option == "Borrow a Book":
        borrow_book()
        input("Press Enter to continue...")
    elif option == "Return a Book":
        return_book()
        input("Press Enter to continue...")
    elif option == "Add a New Book":
        add_book()
        input("Press Enter to continue...")
    elif option == "View Borrowed Books":
        view_borrowed_books()
        input("Press Enter to continue...")
    elif option == "Exit":
        break
    else:
        print("Invalid input")
