from library_manager.inventory import LibraryInventory

def menu():
    print("\n=== Library Inventory Manager ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        try:
            choice = int(input("Enter option: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(title, author, isbn)
            print("Book added successfully.")

        elif choice == 2:
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_data()
                print("Book issued.")
            else:
                print("Cannot issue book!")

        elif choice == 3:
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_data()
                print("Book returned.")
            else:
                print("Cannot return book!")

        elif choice == 4:
            print("\nAll Books:")
            print(inventory.display_all())

        elif choice == 5:
            title = input("Enter title: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No matching books found.")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
