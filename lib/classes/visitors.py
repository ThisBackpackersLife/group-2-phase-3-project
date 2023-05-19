from .__init__ import CONN, CURSOR

class Visitors:
    
    def __init__( self, first_name, last_name, address, id=None ):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.id = id


    @property
    def first_name( self ):
        return self._first_name
    
    @first_name.setter
    def first_name( self, name ):
        if isinstance( name, str ) and len( name ) > 0:
            self._first_name = name
        else:
            raise Exception( "First name must be a string > 0 characters.")
        
    @property
    def last_name( self ):
        return self._last_name
    
    @last_name.setter
    def last_name( self, name ):
        if isinstance( name, str ) and len( name ) > 0:
            self._last_name = name
        else:
            raise Exception( "Last name must be a string > 0 characters.")
        
    @property
    def address( self ):
        return self._address
    
    @address.setter
    def address( self, address ):
        if isinstance( address, str ) and len( address ) > 0:
            self._address = address
        else:
            raise Exception( "Address must be a string > 0 characters.")

    @classmethod
    def create_table( cls ):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS visitors(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                address TEXT
            )
        """
        )
        print( "Check console to verify creation was successful." )

    @classmethod
    def create( cls, first_name, last_name, address ):
        visitor = Visitors( first_name, last_name, address )
        CURSOR.execute(f"""
            INSERT INTO visitors ( first_name, last_name, address )
            VALUES( '{ visitor.first_name }', '{ visitor.last_name }', '{ visitor.address }')
        """
        )
        new_visitor_id = CURSOR.execute( "SELECT last_insert_rowid() FROM visitors" ).fetchone()[0]
        CONN.commit()
        return cls.find_by_id( new_visitor_id )

    @classmethod
    def find_by_id( cls, id ):
        if isinstance( id, int ) and id > 0:
            sql = f"SELECT * FROM visitors WHERE id = { id }"
            new_visitor = CURSOR.execute( sql ).fetchone()
            if new_visitor:
                return cls.db_into_instance( new_visitor )
            else:
                raise Exception( "Could not find Visitor with that ID.")
        else: 
            raise Exception( "ID must be a number > 0." )
        
    @classmethod 
    def find_by_name( cls, name ):
        if isinstance( name, str ) and len( name ) > 0:
            sql = f"SELECT * FROM visitors WHERE first_name LIKE '{ name }' OR last_name LIKE '{ name }'"
            visitors = CURSOR.execute( sql ).fetchall()
            if visitors:
                return [ cls.db_into_instance( visitor ) for visitor in visitors ]
            else:
                raise Exception( "Could not find any visitors with that name." )
        else:
            raise Exception( "Last name must be a string > 0 characters.")


    @classmethod
    def all ( cls ):
        sql = "SELECT * FROM visitors"

        visitors = CURSOR.execute( sql ).fetchall()
        return [ cls.db_into_instance( visitor  ) for visitor in visitors ]

    @classmethod
    def db_into_instance( cls, visitor ):
        return Visitors( visitor[1], visitor[2], visitor[3], visitor[0] )