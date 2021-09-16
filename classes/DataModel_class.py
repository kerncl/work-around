class Descriptor:
    def __init__(self, name=None, **opts):
        print(f'** Called __init__({name!r}, {opts!r}) from {self.__class__}')
        self._name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        print(f'** Called __set__({instance!r}, {value!r}) from {self.__class__}')
        instance.__dict__[self._name]=value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        print(f'** Called __set__({instance!r}, {value!r}) from {self.__class__}')
        if not isinstance(value, self.expected_type):
            raise TypeError('expected' + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        print(f'** Called __set__({instance!r}, {value!r}) from {self.__class__}')
        if value < 0:
            raise ValueError('Expected >=0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        print(f'** Called __init__({name!r}, {opts!r}) from {self.__class__}')
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        print(f'** Called __set__({instance!r}, {value!r}) from {self.__class__}')
        if len(value)>= self.size:
            raise ValueError('Size must be <' + str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    print(f'Called Integer class')
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    print(f'Called UnsignedInteger class')
    pass


class Float(Typed):
    print(f'Called Float class')
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    print(f'Called UnsignedFloat class')
    pass


class String(Typed):
    print(f'Called String class')
    expected_type = str


class SizeString(String, MaxSized):
    print(f'Called SizeString class')
    pass


class Stock:
    name = SizeString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)