class Employee:
    'Common base class for all employees'   #access by --> ClassName.__doc__
    empCount = 0    #class variable --> shared among all instance of a class**
                    #               --> can be access by inside the class or outside the class (exp Employee.empCount)

    def __init__(self, name, salary):   #class constructor
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print('Total Employee %d' %Employee.empCount)

    def displayEMployee(self):
        print('Name:', self.name, ', Salary:', self.salary)

#Create Instance Object
'This would be create first object of Employee class'
emp1 = Employee('Zara', 2000)   #   emp1 --> object
'This would be create 2nd object of Employee class'
emp2 = Employee('Manni', 500)   # emp2 --> object

#Accessing Attributes
emp1.displayEMployee()
emp2.displayEMployee()
print('Total Employee %d' %Employee.empCount)   #Total Employee is 2 (becuase class variable access 2 time)

emp1.age=7  #add an 'age' attribute
print(emp1.age)
emp1.age=8  #modify 'age' attribute
print(emp1.age)
del emp1.age    #delete 'age' attribute
print(hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
print(getattr(emp1, 'age'))    # Returns value of 'age' attribute
delattr(emp1, 'age')    # Delete attribute 'age'

#Built in class attribute
print ("Employee.__doc__:", Employee.__doc__)   #document of the class
print ("Employee.__name__:", Employee.__name__) #class name
print ("Employee.__module__:", Employee.__module__) #currently running at which module
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

#Data Hiding
class JustCounter:
    __secretCount = 0
    _secretCounts = 0
    def count(self, cnt):
        self.__secretCount+=1
        self.cnt = cnt
        print(self.__secretCount)

counter = JustCounter()
counter.count(1)
counter.count(1)
print(counter._JustCounter__secretCount)    #print the secret value in class (object._className__secretCount)