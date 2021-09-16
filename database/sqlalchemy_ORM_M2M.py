from sqlalchemy import create_engine
from sqlalchemy import String, ForeignKey, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///sqlalchemy_ORM_M2M.db', echo=True)


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship('Employee', secondary='link')


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    departments = relationship('Department', secondary='link')


class Link(Base):
    __tablename__ = 'link'
    department_id = Column(Integer, ForeignKey('department.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)


# Create DB
Base.metadata.create_all(engine)

d1 = Department(name="Accounts")
d2 = Department(name="Sales")
d3 = Department(name="Marketing")

e1 = Employee(name="John")
e2 = Employee(name="Tony")
e3 = Employee(name="Graham")

e1.departments.append(d1)
e2.departments.append(d3)
d1.employees.append(e3)
d2.employees.append(e2)
d3.employees.append(e1)
e3.departments.append(d2)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
session.add(e1)
session.add(e2)
session.add(d1)
session.add(d2)
session.add(d3)
session.add(e3)
session.commit()


result = session.query(Department, Employee)\
    .filter(Link.department_id==Department.id, Link.employee_id == Employee.id)\
    .order_by(Link.department_id).all()

for x in result:
    print(f'Department: {x.Department.name} Name: {x.Employee.name}')
