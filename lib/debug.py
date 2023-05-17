from classes.library import Library
from classes.books import Books
from classes.visitors import Visitors

from faker import Faker

faker = Faker()

import ipdb

Visitors.create_table()

for n in range( 0, 5 ):
    Visitors.create( faker.first_name(), faker.last_name(), faker.address() )


ipdb.set_trace()