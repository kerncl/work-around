class Mutable(object):
    def __init__(self, a, b):
        print(f'** Called __init__({a!r}, {b!r}) from {self.__class__}')
        self.a = a
        self.b = b


class Immutable(Mutable):
    def __new__(cls, *args, **kwargs):
        print(f'** Called __new__({args!r}, {kwargs!r})')
        thing = Mutable(*args, **kwargs)
        print(f'initial thing : {thing.__class__}')
        thing.__class__ = cls
        return thing

    def __init__(self, a, b):
        print(f'** Called __init__({a!r}, {b!r}) from {self.__class__}')

    def __setattr__(self, key, value):
        print(f'** Called __setattr__({key!r}, {value!r})')
        raise AttributeError("Sorry Children cant")


im = Immutable(2,3)
print(im.a, im.b, sep=', ')