from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import text, select, and_, join, or_, asc, desc
from sqlalchemy import union, union_all, except_, intersect
from sqlalchemy.sql import update, func

engine = create_engine('sqlite:///sqlalchemy_template.db', echo=True)
meta = MetaData()

## Table
students = Table(
    'students', meta,
    Column('id', Integer, primary_key= True),
    Column('name', String),
    Column('lastname', String)
)
address = Table(
    'address', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('postal_add', String),
    Column('email_add', String)
)

## Create all defined table objects and stores the information in metadata
meta.create_all(engine)   # MyNotes: Only be used during first time
conn = engine.connect()

## Insert Single data at one time
# ins = students.insert()
# ins = students.insert().values(name='Ravi', lastname='Kapoor')
# result = conn.execute(ins)


# Drop table before start
drop_students = students.delete()
conn.execute(drop_students)
drop_address = address.delete()
conn.execute(drop_address)


## Insert Multiple Data at one time
conn.execute(students.insert(), [
    {'name': 'Ravi', 'lastname': 'Kapoor'},
    {'name': 'Rajiv', 'lastname': 'Khanna'},
    {'name': 'Komal', 'lastname': 'Bhandari'},
    {'name': 'Abdul', 'lastname': 'Sattar'},
    {'name': 'Priya', 'lastname': 'Rajhans'},
])

conn.execute(address.insert(), [
    {'st_id': 1, 'postal_add': 'Shivajinagar Pune', 'email_add': 'ravi@gmail.com'},
    {'st_id': 1, 'postal_add': 'ChurchGate Mumbai', 'email_add': 'kapoor@gmail.com'},
    {'st_id': 3, 'postal_add': 'Jubilee Hills Hyderabad', 'email_add': 'komal@gmail.com'},
    {'st_id': 5, 'postal_add': 'MG Road Bangaluru', 'email_add': 'as@yahoo.com'},
    {'st_id': 2, 'postal_add': 'Cannought Place new Delhi', 'email_add': 'admin@khanna.com'},
])

## Select * FROM TABLE  ##

# Select single TABLE
s = students.select()
conn = engine.connect()
result = conn.execute(s)
[print(row) for row in result]

s = students.select().where(students.c.id>2)
result = conn.execute(s)
[print(row) for row in result]

# Select Multiple Table
s = select([students, address]).where(students.c.id == address.c.st_id)
result = conn.execute(s)
[print(row) for row in result]

## Executed using text  ##
s = text("select students.name, students.lastname from students where students.name between :x and :y")
result = conn.execute(s, x='A', y='L').fetchall()
[print(row) for row in result]

s = select([text("students.name, students.lastname from students")])\
    .where(text("students.name between :x and :y"))
result = conn.execute(s, x='A', y='L').fetchall()
[print(row) for row in result]

s = select([text("* from students")])\
    .where(
        and_(
            text("students.name between :x and :y"),
            text("students.id>2")
        )
)
result = conn.execute(s, x='A', y='L').fetchall()
[print(row) for row in result]

## Update Table ##
stmt = students.update().where(students.c.lastname=='Khanna').values(lastname='Kappor')
conn.execute(stmt)
s = students.select()
result = conn.execute(s).fetchall()
[print(row) for row in result]

stmt = update(students).where(students.c.lastname == 'Khanna').values(lastname= 'Kapoor')
conn.execute(stmt)
s = students.select()
result = conn.execute(s).fetchall()
[print(row) for row in result]

## Delete   ##
stmt = students.delete().where(students.c.lastname == 'Khanna')
conn.execute(stmt)
result = conn.execute(text("SELECT * FROM students")).fetchall()
[print(row) for row in result]

## Join ##
j = students.join(address, students.c.id == address.c.st_id)
stmt = select([students]).select_from(j)
result = conn.execute(stmt).fetchall()
[print(row) for row in result]

## AND ##
stmt = select([students]).where(
    and_(students.c.name == 'Ravi', students.c.id<3)
)
result = conn.execute(stmt)
[print(row) for row in result]

## OR ##
stmt = select([students]).where(
    or_(students.c.name == 'Ravi', students.c.id<3)
)
result = conn.execute(stmt)
[print(row) for row in result]

## Order by ##
# ascending
stmt = select([students]).order_by(asc(students.c.name))
result = conn.execute(stmt)
[print(row) for row in result]

# descending
stmt = select([students]).order_by(desc(students.c.name))
result = conn.execute(stmt)
[print(row) for row in result]


## Function ##
# result = conn.execute(select([func.avg(students.c.id)])).fetchnone()
# print(result)


## Set ##
# Union
u = union(address.select().where(address.c.email_add.like("%@gmail.com")),
            address.select().where(address.c.email_add.like('%@yahoo.com')))
result = conn.execute(u).fetchall()
[print(row) for row in result]
# Union all
u = union_all(address.select().where(address.c.email_add.like('%@gmail.com')),
            address.select().where(address.c.email_add.like('%@yahoo.com')))
result = conn.execute(u).fetchall()
[print(row) for row in result]
# except
u = except_(address.select().where(address.c.email_add.like('%@gmail.com')),
            address.select().where(address.c.postal_add.like('%Pune')))
result = conn.execute(u).fetchall()
[print(row) for row in result]
# intersect
u = intersect(address.select().where(address.c.email_add.like('%@gmail.com')),
              address.select().where(address.c.postal_add.like('%Pune')))
result = conn.execute(u).fetchall()
[print(row) for row in result]
print()