from classes.library import Library
from classes.books import Books
from classes.visitors import Visitors

from faker import Faker
import random 

faker = Faker()

import ipdb

Visitors.create_table()
Library.create_table()
Books.create_table()

# for n in range( 0, 5 ):
#     Visitors.create( faker.first_name(), faker.last_name(), faker.address() )

# for n in range( 0, 5 ):
#     Library.create( f"Library { faker.city() }", faker.city()  )

# for n in range( 0, 5 ):
#     Books.create( "Some Book Someone Totally Wrote", f"{faker.first_name()} {faker.last_name()}", random.choice([0,1]), 1, 1 )

ipdb.set_trace()