from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, subqueryload, joinedload
from sqlalchemy.sql import func


engine = create_engine('sqlite:///sqlalchemy_ORM_relationship.db', echo=True)
Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customers", back_populates = "invoices")


# Create DB
Customers.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer", cascade="all,delete, delete-orphan")
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Clear data
session.query(Customers).delete()
session.query(Invoice).delete()
session.commit()

# Relationship
c1 = Customers(name="Gopal Krishna",
               address="Bank Street Hydarebad",
               email="gk@gmail.com")
c1.invoices = [Invoice(invno=10, amount=15000), Invoice(invno=14, amount=3850)]

session.add(c1)
session.commit()

rows = [
   Customers(
      name="Govind Kala",
      address="Gulmandi Aurangabad",
      email="kala@gmail.com",
      invoices=[Invoice(invno=7, amount=12000), Invoice(invno= 8, amount=18500)]),

   Customers(
      name="Abdul Rahman",
      address="Rohtak",
      email="abdulr@gmail.com",
      invoices=[Invoice(invno=9, amount=15000),Invoice(invno=11, amount=6000)])
]
session.add_all(rows)
session.commit()

# Joins
for c, i in session.query(Customers, Invoice).filter(Customers.id == Invoice.custid).all():
   print ("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id, c.name, i.invno, i.amount))
result = session.query(Customers).join(Invoice).filter(Invoice.amount == 8500)
for row in result:
   for inv in row.invoices:
      print (row.id, row.name, inv.invno, inv.amount)

stmt = session.query(Invoice.custid, func.count('*').label('invoice_count')).group_by(Invoice.custid).subquery()
for u, count in session.query(Customers, stmt.c.invoice_count)\
                            .outerjoin(stmt, Customers.id == stmt.c.custid)\
                            .order_by(Customers.id):
   print(u.name, count)


## Relationship operators
# Not equal
s = session.query(Customers).filter(Invoice.custid.__ne__(2))
print(s) # print SQL command
[print(f'ID: {row.id}, name: {row.name}, address: {row.address}, email: {row.email}') for row in s.all()]
# Equal
s = session.query(Customers).filter(Invoice.custid.__eq__(2))
print(s)
[print(f'ID: {row.id}, name: {row.name}, address: {row.address}, email: {row.email}') for row in s.all()]
# contains
s = session.query(Invoice).filter(Invoice.invno.contains([3, 4, 5]))
print(s)
# [print(f'ID: {row.id}, custid: {row.invno}, amount: {row.amount}') for row in s.all()]
# any
s = session.query(Customers).filter(Customers.invoices.any(Invoice.invno == 11))
print(s)
[print(f'ID: {row.id}, name: {row.name}, address: {row.address}, email: {row.email}') for row in s.all()]
# has
s = session.query(Customers).filter(Invoice.customer.has(name = 'Arjun Pandit'))
print(s)
[print(f'ID: {row.id}, name: {row.name}, address: {row.address}, email: {row.email}') for row in s.all()]


## Subquery load
c1 = session.query(Customers).options(subqueryload(Customers.invoices)).filter_by(name = 'Govind Pant').all()
# print(c1.name, c1.address, c1.email)
# for x in c1.invoices:
#     print(f"Invoice no: {x.invno}, Amount: {x.amount}")
[print(x) for x in c1]
# Joined load
c1 = session.query(Customers).options(joinedload(Customers.invoices)).filter_by(name='Govind Pant').all()
[print(x) for x in c1]

# Delete related object
x = session.query(Customers).get(2)
session.delete(x)
session.commit()
result = session.query(Customers).get(2)
print(result)
