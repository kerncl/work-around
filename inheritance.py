class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        self.fn = self.first + self.last
        return self.fn

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        # super().__init_(self,first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amt = 1.2

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.empployees.append(emp)

    def remoove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


employee1 = Employee('Chin', 'LinnKern', 3500)
employee2 = Employee('Lim', 'ZhiQing', 3500)
dev1 = Developer('Jason', 'Lim', 3350, 'python')
manager1 = Manager('Hong', 'LingZhen', 10000, [employee1])
manager2 = Manager('Jess', 'Kiu', 10000, [employee2])
print(employee1.fullname())
print(employee1.apply_raise())
print(employee2.fullname())
print(employee2.apply_raise())
print(dev1.email)
print(dev1.prog_lang)
print(manager1.email)
print(manager1.apply_raise())
manager1.print_emp()
print(manager2.email)
print(manager2.apply_raise())
manager2.print_emp()

print(isinstance(manager1, Employee))
print(isinstance(dev1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Employee, Manager))
