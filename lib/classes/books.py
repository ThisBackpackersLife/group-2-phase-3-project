from .__init__ import CONN, CURSOR


class Books:
    
    def __init__( self, title, author, checked_out, library_id, visitor_id, id = None ):

        self.title = title
        self.author = author
        self.checked_out = checked_out
        self.library_id = library_id
        self.visitor_id = visitor_id

    @property
    def title( self ):
        return self._title
    
    @title.setter
    def title( self, title ):
        if isinstance( title, str ) and len( title ) > 0:
            self._title = title
        else:
            raise Exception("Title must be a string greater than 0 characters.")

    @property
    def author( self ):
        return self._author
    
    @author.setter
    def author( self, author ):
        if isinstance( author, str ) and len( author ) > 0:
            self._author = author
        else:
            raise Exception("Author must be a string greater than 0 characters.")
        
    @property
    def checked_out(self):
        if self._checked_out :
            return print("Book is available for check out!")
        else:
            return print("Book is unavailable, it has been checked out.")


    @checked_out.setter
    def checked_out(self, checked_out):
        if checked_out:
            self._checked_out = 1
        else:
            self._checked_out = 0

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                checked_out INTEGER,
                library_id INTEGER,
                visitor_id INTEGER,
                    FOREIGN KEY ( library_id ) REFERENCES library( id ),
                    FOREIGN KEY ( visitor_id ) REFERENCES visitors( id )
                )
        """
        )
        print("Table creation attempted")


    @classmethod
    def create ( cls, title, author, checked_out, library_id, visitor_id ):
        new_book = Books( title, author, checked_out, library_id, visitor_id )
        if new_book:
            sql = f"""
                INSERT INTO books ( title, author, checked_out, library_id, visitor_id )
                VALUES ( "{new_book.title}", "{new_book.author}", {checked_out}, {new_book.library_id}, {new_book.visitor_id} )
            """
            CURSOR.execute( sql )
            app_id = CURSOR.execute( 'SELECT last_insert_rowid() FROM books' ).fetchone()[0]
            new_app = CURSOR.execute( f'SELECT * FROM books WHERE id = { app_id }' ).fetchone()
            CONN.commit()
            return new_app
        else :
            raise Exception( 'Could not create book. Check data and try again.' )
        
    @classmethod
    def find_by_id( cls, id ):
        if isinstance( id, int ) and id > 0:
            sql = f"SELECT * FROM books WHERE id = { id }"
            new_book = CURSOR.execute( sql ).fetchone()
            if new_book:
                return cls.db_into_instance( new_book )
            else:
                raise Exception( "Could not find Book with that ID.")
        else: 
            raise Exception( "ID must be a number > 0." )
        
    @classmethod
    def update( cls, id, title=None, author=None ):
        book = cls.find_by_id( id )
        if book:
            if title is not None:
                book.title = title
            if author is not None:
                book.author = author
            else:
                raise Exception( "Attribute must be provided for an update." )
            
            sql = f"""
                UPDATE books SET
                title = "{ book.title }",
                author = "{ book.author }"
                WHERE id = { id }
            """
            CURSOR.execute( sql )
            CONN.commit()
            print( "Book information has been updated successfully!" )
        else:
            raise Exception( "Could not find Book with that ID." )

    @classmethod
    def all ( cls ) :
        sql = "SELECT * FROM books"
        
        apps = CURSOR.execute( sql ).fetchall()
        return apps

    @classmethod
    def db_into_instance( cls, book ):
        return Books( book[1], book[2], book[3], book[4], book[5], book[0] )