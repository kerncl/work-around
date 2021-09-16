from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name
    # def __set_name__(self, owner, name):
    #     print(f'Called __set_name__ ({owner!r}, {name!r})')
    #     self.name = name

    def __set__(self, instance, value):
        print(f'Called __set__ ({instance!r}, {value!r})')
        if not instance(value, self._expected_type):
            raise TypeError('Expected' + str(self._expected_type))
        instance.__dict__[self._name]=value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        print(f'Called __new__ ({cls!r}, {clsname!r}, {bases!r}, {clsdict!r})')
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)

        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        print(f'Called __prepare__ ({metacls!r}, {name!r}, {bases!r})')
        return OrderedDict()


class OrderedMeta2(type):
    def __new__(cls, clsname, bases, clsdict):
        print(f'Called __new__ ({cls!r}, {clsname!r}, {bases!r}, {clsdict!r})')
        return type.__new__(cls, clsname, bases, clsdict)

    @classmethod
    def __prepare__(metacls, name, bases):
        print(f'Called __prepare__ ({metacls!r}, {name!r}, {bases!r})')
        return OrderedDict().__dict__


class Stock(metaclass=OrderedMeta):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class Stock2(metaclass=OrderedMeta2):
    # name = String()
    # shares = Integer()
    # price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('Goog', 100, 490.1)
s2 = Stock2('Goog2', 100, 490.1)