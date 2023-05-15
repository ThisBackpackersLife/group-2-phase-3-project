from classes.library import Library
from classes.books import Books
from classes.visitors import Visitors
from classes.__init__ import CONN, CURSOR


def main():

    print("yeah")

    choice = 0
    while choice !=7:
        print("""
    Welcome to 'Book It To The Library'!
Please type in the number corresponding to the choice.
--------------------------------------------------------""")
        print("1) Add new book")
        print("2) New visitor? Let's get you set up :)")
        print("3) Add new library")
        print("4) View books")
        print("5) View libraries")
        print("6) Update visitor information.")
        print("7) Quit.")
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
            Books.all()

        elif choice == 5:
            all_libraries = list( Library.all() )
            for l in all_libraries:
                print( f"""id:  { l.id }, name:  { l.name }""" )

        elif choice == 6:
            print("""
    To update visitor please enter visitor's updated first name, last name, and address in the appropriate inputs.
            """)
            id = input("Please enter visitor id. >>>")
            first_name = input("Please enter first name. >>>")
            last_name = input("Please enter last name. >>>")
            address = input("Please enter address. >>>")

            int_id = int(id)

            Visitors.update(int_id, first_name, last_name, address)
            print(f"""
    Hello {first_name}! Your information has been updated.""")

if __name__ == "__main__":
    main()