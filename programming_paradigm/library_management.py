# library_management.py

class Book:
    """Represents a book with title, author, and checkout status."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Return True if the book is available, False if checked out."""
        return not self._is_checked_out

    def __str__(self):
        """Return a readable string for the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book: Book):
        """Add a Book instance to the library collection."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title: str):
        """Return a book by title if it exists in the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or not checked out

    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
