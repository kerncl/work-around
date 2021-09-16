a =5
b =6
print(a+b)
print(int.__add__(a,b))

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

#Those __<pre-define>__ called magic method
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)     #s3 is an object
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}' .format(self.m1, self.m2)

s1 = student(58,69)
s2 = student(60,64)

#Addition
s3 = s1 + s2
print(s3.m1)
print('\n')
#Greater
if s1>s2:
    print('S1 greater')
else:
    print('S2 greater')
print('\n')

#print object
a =9
print(a)    #print(a.__str__())
print(s1)