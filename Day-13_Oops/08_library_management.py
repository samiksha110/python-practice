
class Library:

    def __init__(self):
        self.books = []

    def add_book(self):

        book = input("Enter Book Name: ")

        self.books.append(book)
    print("Book Added Successfully!")

    def view_books(self):

        if len(self.books) == 0:
            print("No books available.")

        else:
            print("\n===== Books =====")
            for book in self.books:
                print(book)

    def search_book(self):

        book = input("Enter Book Name: ")

        if book in self.books:

            print("Book Found!")

        else:
            print("Book Not Found!")

    def remove_book(self):

        book = input("Enter Book Name: ")

        if book in self.books:

            self.books.remove(book)

            print("Book Removed Successfully!")

        else:

            print("Book Not Found!")


library = Library()

while True:

    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.view_books()

    elif choice == 3:
        library.search_book()

    elif choice == 4:
        library.remove_book()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
