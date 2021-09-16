from functools import wraps
from string import digits


def showinfo(method):
    wraps(method)

    def wrapper(*args, **kwargs):
        print(f'{method.__name__}{args}')
        return_val = method(*args, **kwargs)
        return return_val
    return wrapper


class Sayhi(object):

    @showinfo
    def __get__(self, instance, owner):
        return 'hi ' + instance.name

    @showinfo
    def __set__(self, instance, value):
        pass


class PublicAttribute(object):

    @showinfo
    def __get__(self, instance, owner):
        return 'Get PublicAttribute'


class A:
    public = 'public attribute'

    sayhi = Sayhi()

    @showinfo
    def __init__(self, name):
        self.name = name
        self.instance = 'instance attribute'
        # self.sayhi = 'hello'

    # @showinfo
    # def __getattribute__(self, item):
    #     return super().__getattribute__(item)

    @showinfo
    def __getattr__(self, item):
        if item[0] not in digits:
            self.__setattr__(item, None)
            print(f'We dont have this instance but we help you to create a new attribute for {item!r}')
        else:
            raise AttributeError(f'Sorry this instance doesnt have this attribute {item!r} '
                                 f'and we dont want to create an attribute start with number')

    # def __setattr__(self, key, value):
    #     setattr(self, key, value)
    #     # super().__setattr__(key, value)

    @showinfo
    def __getitem__(self, item):
        return self.__dict__[item]

    def do_A(self):
        print('do A')

    def do_B(self):
        print('do B')

    def do_C(self):
        print('do C')


if __name__ == '__main__':
    a = A('lk')
    print(a.name)
    print(A.public)
    print(a.age)
    print(a.sayhi)
