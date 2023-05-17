from . import CONN, CURSOR

class Library:
    
    def __init__( self, name, city, id=None ):
        self.name = name
        self.city = city
        self.id = id

    @property
    def name( self ):
        return self._name
    
    @name.setter 
    def name( self, name ):
        if isinstance( name, str ) and len( name ) > 0:
            self._name = name
        else:
            raise Exception( "Name must be a string > 0." )
        
    @property
    def city( self ):
        return self._city

    @city.setter
    def city( self, city ):
        if isinstance( city, str ) and len( city ) > 0:
            self._city = city
        else:
            raise Exception( "City must be a string > 0." )

    @classmethod
    def create_table( cls ):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS libraries(
                id INTEGER PRIMARY KEY,
                name TEXT,
                city TEXT
            )
        """
        )
        print( "Check console to verify creation was successful." )

    @classmethod
    def create( cls, name, city ):
        library = Library( name, city )
        CURSOR.execute(f"""
            INSERT INTO libraries( name, city )
            VALUES( '{ library.name }', '{ library.city }')
        """
        )
        new_library_id = CURSOR.execute( "SELECT last_insert_rowid() FROM libraries" ).fetchone()[0]
        CONN.commit()
        return cls.find_by_id( new_library_id )

    @classmethod
    def find_by_id( cls, id ):
        if isinstance( id, int ) and id > 0:
            sql = f"SELECT * FROM libraries WHERE id = { id }"
            new_library = CURSOR.execute( sql ).fetchone()
            if new_library:
                return cls.db_into_instance( new_library )
            else:
                raise Exception( "Could not find Library with that ID.")
        else: 
            raise Exception( "ID must be an number > 0." )
        
    @classmethod 
    def find_by_name( cls, name ):
        if isinstance( name, str ) and len( name ) > 0:
            sql = f"SELECT * FROM libraries WHERE name LIKE '{ name }'"
            libraries = CURSOR.execute( sql ).fetchall()
            if libraries:
                return [ cls.db_into_instance( library ) for library in libraries ]
            else:
                raise Exception( "Could not find any libraries with that name." )
        else:
            raise Exception( "Name must be a string > 0 characters." )


    @classmethod
    def all ( cls ):
        sql = "SELECT * FROM libraries"

        libraries = CURSOR.execute( sql ).fetchall()
        return [ cls.db_into_instance( library ) for library in libraries ]

    @classmethod
    def db_into_instance( cls, library ):
        return Library( library[1], library[2], library[0] )
    
    