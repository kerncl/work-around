class Foo(object):
    def __new__(cls, *args, **kwargs):
        print('Creating instance')
        instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, a, b, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.b = b

    def bar(self):
        pass


if __name__ == '__main__':
    i = Foo(2,3)