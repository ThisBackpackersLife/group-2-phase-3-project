from classes.library import Library
from classes.books import Books
from classes.visitors import Visitors

from faker import Faker

faker = Faker()

import ipdb

Visitors.create_table()
Library.create_table()

for n in range( 0, 5 ):
    Visitors.create( faker.first_name(), faker.last_name(), faker.address() )

for n in range( 0, 5 ):
    Library.create( f"Library { faker.city() }", faker.city()  )

ipdb.set_trace()