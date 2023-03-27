def main():
    try:
        booklist = create_booklist()
        menu(booklist)
    except FileNotFoundError:
        print("Error: bestsellers.txt not found")

def create_booklist():
    booklist = []
    with open("bestsellers.txt") as f:
        for line in f:
            title, author, publisher, date, category = line.strip().split("\t")
            year, month, _ = date.split("/")
            booklist.append((title, author, publisher, int(year), int(month), category))
    return booklist

def display_books(books):
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"{book[0]} by {book[1]} ({book[3]}/{book[4]}, {book[5]})")

def menu(booklist):
    while True:
        print("Menu:")
        print("1. Display all books in a year range")
        print("2. Display all books in a specific month and year")
        print("3. Search for an author")
        print("4. Search for a title")
        print("Q. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            start_year = int(input("Enter starting year: "))
            end_year = int(input("Enter ending year: "))
            books = [book for book in booklist if start_year <= book[3] <= end_year]
            display_books(books)

        elif choice == "2":
            month = int(input("Enter month: "))
            year = int(input("Enter year: "))
            books = [book for book in booklist if book[3] == year and book[4] == month]
            display_books(books)

        elif choice == "3":
            search_string = input("Enter author search string: ").lower()
            books = [book for book in booklist if search_string in book[1].lower()]
            display_books(books)

        elif choice == "4":
            search_string = input("Enter title search string: ").lower()
            books = [book for book in booklist if search_string in book[0].lower()]
            display_books(books)

        elif choice == "q":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
