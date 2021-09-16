import math


class myclass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r}'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


class Pizza2:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r} '
                f'{self.ingredients!r}')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r**2*math.pi


if __name__ == '__main__':
    obj = myclass()
    print(obj.method())
    print(myclass.method('a'))  #object: a
    print(myclass.method(obj))
    print(obj.classmethod())
    print(myclass.classmethod())
    print(obj.staticmethod())

    print('\n')
    print('withthout creating a an instance object')
    print(myclass.classmethod())
    print(myclass.staticmethod())
    try:
        print(myclass.method())
    except:
        print('unable to call class method')

    print('\n')
    print(Pizza(['cheese', 'tomatoes']))
    print(Pizza.margherita())
    print(Pizza.prosciutto())

    print('\n')
    p=Pizza2(4, ['mozzarella', 'tomatoes'])
    print(p)
    print(p.area())
    print(Pizza2.circle_area(4))