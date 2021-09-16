class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:   #able to execute when only 2 input
            s=a+b
        else:
            s=a
        return s

s1 = student(58,69)

print(s1.sum(1,2))
print('\n')

class A:
    def show(self):
        print('in A show')

class B(A):
    def show (self):
        print('in B show')

a1 = A()
b1 = B()
a1.show()
b1.show()
