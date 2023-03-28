import re

def search_books_by_year():
    book_file = open('bestsellers.txt', 'r')
    start_year = str(input("Enter starting year: "))
    end_year = str(input("Enter ending year: "))

    for line in book_file.readlines():
        line = line.split("\t")
        date = line[3]
        y = date.split("/")
        year = y[2]

        if start_year <= year <= end_year:
            print(f'"{line[0]}" by {line[1]} pub date: {line[3]}')
def search_books_by_year_and_month():
    book_file = open('bestsellers.txt', 'r')

    x = True

    while x:

        try:
            month_input = int(input("Enter month (1-12): "))
            year_input = int(input("Enter year: "))

            for line in book_file:
                line = line.split("\t")
                dates = line[3]
                specific_date = dates.split("/")

                month = specific_date[0]
                year = specific_date[2]

                if month_input == int(month) and year_input == int(year):
                    print(f'"{line[0]}" by {line[1]} pub date: {line[3]}')
            x = False
        except ValueError:
            print("I don't understand this commmand")
    book_file.close()

def search_books_by_author():
    book_file = open('bestsellers.txt', 'r')
    count = 0
    name = input('Enter search string: ')

    for line in book_file:
        title = line.split("\t")[0]
        author = line.split("\t")[1]
        date = line.split("\t")[3]

        search = author.lower()

        match = re.search(name, search)

        if match:
            print(title + " by: " + author + "(pub date: " + date + ")")
            count += 1

    if count == 0:
        print("No books found.")


def search_books_by_title():
    book_file= open('bestsellers.txt', 'r')
    title_list = []
    num_books = book_file.readlines()
    book_file.close()

    for book in num_books:
        book = book.rstrip('\n')

        x = book.split('\t')
        title_list.append(x[0])

    search_string = str(input('Enter search string: '))
    search_string = search_string.lower()
    match_list = []

    for title in title_list:
        if search_string in title.lower():
            match_list.append(title)
    print()

    for matched_title in match_list:
        print(matched_title)
def main():
    best_sellers = open('bestsellers.txt', 'r')

    num_books = 0

    for x in best_sellers:
        num_books += 1

    print("\nRead", str(num_books), "books")

    y = True
    while y:
        r_input = input(str("""\nWhat would you like to do?
        1. Look up year range
        2. Look up month/year
        3. Search for author
        4. Search for title
        Q. Quit
        """))

        if r_input.lower() == '1' or r_input.lower() == 'look up year range':
            search_books_by_year()
            
        elif r_input.lower() == '2' or r_input.lower() == 'look up month/year':
            search_books_by_year_and_month()
            
        elif r_input.lower() == '3' or r_input.lower() == 'search for author':
            search_books_by_author()
            
        elif r_input.lower() == '4' or r_input.lower() == 'search for title':
            search_books_by_title()

        elif r_input.lower() == 'q' or r_input.lower() == 'quit':
            print("Done")
            break
        else:
            print("Enter a valid choice ")

if __name__ == '__main__':
    main()
