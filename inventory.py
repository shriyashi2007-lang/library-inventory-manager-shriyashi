import json
import logging
from pathlib import Path
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if not self.file_path.exists():
                self.save_data()
                return

            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.books = [Book(**entry) for entry in data]

        except Exception as e:
            logging.error(f"Error loading catalog: {e}")
            print("Error reading catalog file! Creating a new one.")
            self.save_data()

    def save_data(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump([b.to_dict() for b in self.books], file, indent=4)
        except Exception as e:
            logging.error(f"Error saving catalog: {e}")

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        logging.info(f"Added book: {title}")
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return "\n".join(str(b) for b in self.books)
