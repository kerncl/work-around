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
        print('Inside Employee Class')
        return self.pay

    def inform(self):
        self.information = self.apply_raise()
        print(self.information)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        #super().__init(self, first, last, pay)
        self.prog_lang = prog_lang

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        print('Inside Developer')

    def inform(self):
        self.information = self.apply_raise()
        print(self.information)


class Manager(Employee):
    raise_amt = 1.15

    def __init__(self, first, last, pay, employee=None):
        Employee.__init__(self, first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print('-->', emp.fullname())

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        print('Inside Manager')


    def inform(self):
        self.information = self.apply_raise()
        print(self.information)


class CEO(Manager):
    raise_amt = 1.3

    def __init__(self, first, last, pay, employee=None):
        Manager.__init__(self, first, last, pay)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        print('Inside CEO')

    def inform(self):
        self.information = self.apply_raise()
        print(self.information)

employee_1 = Employee('Chin', 'LinnKern', 3500)
employee_2 = Employee('Lim', 'ZhiQing', 3500)
dev_1 = Developer('Jason', 'Lim', 3500, 'python')
manager_1 = Manager('Khoo', 'JM', 20000)
manager_2 = Manager('HOng', 'Ling Zhen', 20000, [employee_1])
ceo_1 = CEO('Bob', 'swam', 200000)
print(employee_1.email)
print(employee_2.email)
print(dev_1.email)
print(employee_1.apply_raise())
print(employee_1.inform())
#print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print('\n')

print(dev_1.email)
print(dev_1.prog_lang)
print('\n')

print(manager_2.fullname())
print(manager_2.print_emp())
manager_2.remove_emp(employee_1)    #pass in object
print('\n')
print(manager_2.print_emp())
print(manager_1.fullname())
print(manager_1.pay)
print(manager_1.print_emp())
print(manager_1.add_emp(employee_1))
print(manager_1.print_emp())
print('\n')

print(isinstance(employee_1, Employee)) #True
print(isinstance(manager_1,Employee))   #True
print(isinstance(dev_1, Employee))  #False
print(isinstance(dev_1, Developer)) #False
print('\n')
print(issubclass(Manager, Employee))    #True
print(issubclass(Employee, Manager))    #False