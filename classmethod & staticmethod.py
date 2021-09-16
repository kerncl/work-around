class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}' .format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):              # add in addition feature on top of the class
        first, last, pay = emp_str.split('-')  # first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)  # new_emp_1 = Employee(first, last, pay)

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'Employee', 60000)
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

# Classmethod
#print(new_emp_1.fullname())
#print(new_emp_1.email)
emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())
print(new_emp_1.email)

# Staticmethod
import datetime
my_date = datetime.date(2020, 8, 15)
print(Employee.is_working(my_date))
