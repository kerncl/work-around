class Base:
    def __init__(self):
        print('Base.__init__')


class Child1(Base):
    def __init__(self):
        super().__init__()  #Base.__init__(self)
        print('Child1.__init__')


class Child2(Base):
    def __init__(self):
        super().__init__()  #Base.__init__(self)
        print('Child2.__init__')


class Child3(Child1, Child2):
    def __init__(self):
        super().__init__()  #Child1.__init__(self)
        #Child2.__init__(self)
        print('Child3.__init__')

c3 = Child3()
print(Child3.__mro__)


class Ten:
    def adder(self, *args):
        print(sum(args)+10)
        super().adder()

class Hundred:
    def adder(self, *args):
        print(sum(args)+100)


class Experiment(Ten, Hundred):
    pass

e = Experiment()
e.adder(1,2,3)
print(Experiment.__mro__)