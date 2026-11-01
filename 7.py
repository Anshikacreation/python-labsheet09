books = []

while True:
    print("\n--- BOOK MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        print("All Books:")
        for book in books:
            print(book)

    elif choice == "3":
        old = input("Enter book name to update: ")

        if old in books:
            new = input("Enter new book name: ")
            index = books.index(old)
            books[index] = new
            print("Book updated successfully!")
        else:
            print("Book not found.")

    elif choice == "4":
        book = input("Enter book name to delete: ")

        if book in books:
            books.remove(book)
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")