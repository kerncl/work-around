import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        print(f'** called __get__({self!r},{instance!r},{cls!r})')
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2*math.pi*self.radius


c = Circle(4.0)
print(vars(c))
print(c.__dict__)
c.area
print(vars(c))
print(c.__dict__)