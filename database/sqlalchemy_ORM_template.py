from sqlalchemy import Column, Integer, String, and_, or_, text, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///sqlalchemy_ORM.db', echo=True)
Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)



# Create database
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Clear data
session.query(Customers).delete()
session.commit()

# Insert into
c1 = Customers(name='Ravi Kumar', address='Station Road Nanded', email='ravi@gmail.com')
session.add(c1)
session.commit()
session.add_all([
    Customers(name='Komal Pande', address='Koti, Hyderabad', email='komal@gmail.com'),
    Customers(name='Rajender Nath', address='Sector 40, Gurgaon', email='nath@gmail.com'),
    Customers(name='S.M.Krishna', address='Budhwar Peth, Pune', email='smk@gmail.com')
])
session.commit()

# Select
result = session.query(Customers).all()
[print(f'Name: {row.name}, Address: {row.address}, Email:{row.email}') for row in result]

## Update
# Get ID=2
x = session.query(Customers).get(2)
print(f'Name: {x.name}, Address: {x.address}, Email: {x.email}')
x.address = 'Banjara Hills Secunderabad'
session.commit()
# First row
x = session.query(Customers).first()
print(f'Name: {x.name}, Address: {x.address}, Email: {x.email}')
x.name = 'Ravi Shrivastava'
print(f'Name: {x.name}, Address: {x.address}, Email: {x.email}')
session.rollback()
print(f'Name: {x.name}, Address: {x.address}, Email: {x.email}')
# Update all
session.query(Customers).filter(Customers.id != 2)\
    .update({Customers.name: "Mr."+Customers.name},synchronize_session=False)
session.commit()

## Filter
result = session.query(Customers).filter(Customers.id > 2)
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]
# equal
result = session.query(Customers).filter(Customers.id == 2)
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]
# not equal
result = session.query(Customers).filter(Customers.id != 2)
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]
# like
result = session.query(Customers).filter(Customers.name.like('Ra%'))
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]
# in
result = session.query(Customers).filter(Customers.id.in_([1,3]))
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]
# and
result = session.query(Customers).filter(Customers.id > 2, Customers.name.like('Ra%'))
result = session.query(Customers).filter(and_(Customers.id > 2, Customers.name.like('Ra%')))
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]
# or
result = session.query(Customers).filter(or_(Customers.id > 2, Customers.name.like('Ra%')))
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]

# Return list
# all
result = session.query(Customers).all()
[print(f'ID: {row.id}, Name: {row.name}, Address: {row.address}, Email: {row.email}') for row in result]
# first
result = session.query(Customers).first()
print(f'ID: {result.id}, Name: {result.name}, Address: {result.address}, Email: {result.email}')
# one
try:
    session.query(Customers).one()
except Exception as e:
    print(e)
# scalar == one
try:
    result = session.query(Customers).filter(Customers.id == 3).scalar()
    print(f'ID: {result.id}, Name: {result.name}, Address: {result.address}, Email: {result.email}')
except Exception as e:
    print(e)

## Textual
# filter
for cust in session.query(Customers).filter(text("id<3")):
    print(cust.name)
cust = session.query(Customers).filter(text("id=:value")).params(value=1).one()
print(f'ID: {cust.id}, Name: {cust.name}, Address: {cust.address}, Email: {cust.email}')
# statement
stmt = text("SELECT name, id, address, email FROM customers")
stmt = stmt.columns(Customers.id, Customers.name)
cust = session.query(Customers.id, Customers.name).from_statement(stmt).all()
[print(f'ID: {row.id}, Name: {row.name}') for row in cust]


