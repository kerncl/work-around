class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@intel.com'

    @property
    def email(self):
        return '{}.{}@intel.com' .format(self.first, self.last)

    @property   # when call the function no need to include (), access the attribute the method
    def fullname(self):
        return '{} {}' .format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None

emp1 = Employee('chin','linnkern')

print(emp1.first)
emp1.last ='zq'
emp1.fullname = 'lim zq'
print(emp1.last)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname

