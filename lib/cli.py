from classes.library import Library
from classes.books import Books
from classes.visitors import Visitors
from classes.__init__ import CONN, CURSOR
import time

def main():

    print("""
        Welcome to 'Book It To The Library'!
""")

    choice = 0
    while choice !=9:
        time.sleep(5)
        print("""
Please type in the number corresponding to the choice.
--------------------------------------------------------""")
        print("1) Add new book.")
        print("2) New visitor? Let's get you set up :)")
        print("3) Add new library.")
        print("4) View books.")
        print("5) View libraries.")
        print("6) Update visitor information.")
        print("7) Update library information.")
        print("8) Update book information.")
        print("9) Quit.")
        choice = int(input())

        if choice == 1:
            print("""
    To add a new book you will need a title, author, and a library id.""")
            title = input("Enter title of the book you'd like to add >>>")
            author = input("Enter author of the book you'd like to add >>>")
            library_id = input("Enter library id >>>")
            checked_out = 1
            visitor_id = input("Enter your id >>>")
            
            new_book = Books.create(title, author, library_id, checked_out, visitor_id)

            # print(new_book)
            print(f"{title} was added to the books database. :) ")

        elif choice == 2:
            print("""
    To set up please enter your first name, last name, and address in the appropriate inputs.
            """)
            first_name = input("Please enter your first name. >>>")
            last_name = input("Please enter your last name. >>>")
            address = input("Please enter your address. >>>")

            new_visitor = Visitors.create(first_name, last_name, address)

            print(f"""
    Hello {first_name}! You're all set. Your id will be {new_visitor.id}""")

        elif choice == 3:
            print("""
    To set up please enter your first name, last name, and address in the appropriate inputs.
            """)
            name = input("Please enter library's name. >>>")
            city = input("Please enter the city the library is located in. >>>")

            new_library = Library.create(name, city)

            print(f"""
    I bet the people over in {new_library.city} are excited for their new library, "{new_library.name}"
    -> This library's id is {new_library.id}""")

        elif choice == 4:
            print(" id,    title,    author")
            all_books = Books.all()
            for b in all_books:
                print( b )

        elif choice == 5:
            all_libraries = list( Library.all() )
            for l in all_libraries:
                print( f"""id:  { l.id }, name:  { l.name }""" )

        elif choice == 6:
            print("""
    To update visitor please enter visitor's updated first name, last name, and address in the appropriate inputs.
            """)
            id = input("Please enter the visitor's id you wish to change. >>>")
            first_name = input("Please enter updated first name. >>>")
            last_name = input("Please enter updated last name. >>>")
            address = input("Please enter updated address. >>>")

            int_id = int(id)

            Visitors.update(int_id, first_name, last_name, address)
            print(f"""
    {first_name} {last_name}'s information has been updated.""")

        elif choice == 7:
            print("""
    To update library please enter library's updated name and city in the appropriate inputs.
            """)
            id = input("Please enter the library's id you wish to change. >>>")
            name = input("Please enter updated name. >>>")
            city = input("Please enter updated city. >>>")

            int_id = int(id)

            Library.update(int_id, name, city)
            print(f"""
    "{name}" has been updated.""")
            
        elif choice == 8:
            print("""
    To update book please enter the book's updated title and author in the appropriate inputs.
            """)
            id = input("Please enter the book's id you wish to change. >>>")
            title = input("Please enter updated title. >>>")
            author = input("Please enter updated author. >>>")

            int_id = int(id)

            Books.update(int_id, title, author)
            print(f"""
    "{title}" has been updated.""")


if __name__ == "__main__":
    main()