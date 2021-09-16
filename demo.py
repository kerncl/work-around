# __str__
# __repr__

# __get__, __getattr__, __getitem__, __getattribute__

from string import digits

def showinfo(method):

    def wrapper(*args, **kwargs):
        print(f'{method.__name__}{args}')
        return_val = method(*args, **kwargs)
        return return_val
    return wrapper


class Sayhi(object):

    @showinfo
    def __get__(self, instance, owner):
        return 'hi' + instance.name


class Klass:
    public = 'public attr'
    sayhi = Sayhi()

    def __init__(self, name):
        self.name = name
        self.sayhi = 'hello from instance'

    # @showinfo
    # def __getattribute__(self, item):
    #     return super(Klass, self).__getattribute__(item)

    @showinfo
    def __getattr__(self, item):
        if item[0] not in digits:
            self.__setattr__(item, 'new attribute')
            print(f'{item!r} New attribute has been set')
        else:
            raise AttributeError('We dont accept attribute start with digits')

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
    myclass = Klass('lk')