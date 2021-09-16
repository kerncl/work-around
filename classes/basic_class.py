class Klass:

    __instance = None

    def __new__(cls, *args, **kwargs):
        print('** Call __new__ method **')
        print(f' <class.__new__({cls!r}, {args!r}, {kwargs!r})>')
        instance = object.__new__(cls) # == super().__new__(cls)
        print(f'instance: {instance}')
        return instance

    def __init__(self, num=None):
        print(f'** Called __init__ method **')
        self.num = num

    def __call__(self, *args, **kwargs):
        print(f'** Call __call__({args!r}, {kwargs!r}) method **')
        print('Hi you calling me ?')
        pass

    def __del__(self):
        print('** Called __del__ method **')
        print(f'What are you trying to del ?? -->') # todo: Print current instance
        pass

    def __repr__(self):
        print('** Called __repr__ method **')
        return f'{self.__class__}'

    def __str__(self):
        print('** Call __str__ method **')
        return self.__repr__()

    def __bytes__(self):
        print(f'** Called __bytes__ method **')
        return b'bytes string'

    def __lt__(self, other):
        print(f'** Called __lt__({other!r}) method **')
        return self.num < other.num

    def __le__(self, other):
        print('** Called __le__ method **')
        return self.num <= other.num

    def __eq__(self, other):
        print(f'** Called __eq__({other!r}) method **')
        if isinstance(other, type(self)):
            return self.num == other.num
        return NotImplemented

    def __ne__(self, other):
        print(f'** Called __ne__({other!r}) method **')
        return self.num != other.num

    def __gt__(self, other):
        print(f'** Called __gt__({other!r}) method **')
        return self.num > other.num

    def __ge__(self, other):
        print(f'** Called __ge__({other!r}) method **')
        return self.num >= other.num

    def __hash__(self):
        print('** Called __hash__ method **')
        return hash(self.num)

    def __bool__(self):
        print('** Called __bool__ method **')
        return bool(self.num)

    def __getattribute__(self, item):
        print(f'** Called __getattribute__({item!r}) method **')
        try:
            return super().__getattribute__(item)
        except AttributeError:
            print('You will be meet my bro __getattr__')
            raise AttributeError

    def __getattr__(self, item):
        print(f'** Called __getattr__({item!r}) method **')
        if item in self.__dict__:
            return self.__dict__.get(item)
        else:
            if input('WatchOut you will getting AttributeError SOON\n'
                     ' listen carefully do you want this attr ?') == 'yes':
                val = input('So, what is it value ?')
                self.__setattr__(item, val)
            else:
                print('Bye ~ AttributeError is OTW')
                raise AttributeError

    def __setattr__(self, key, value):
        print(f'** Called __setattr__({key!r}, {value!r}) method **')
        # super(Klass, self).__setattr__(key, value)
        # self.__dict__.update({key: value})
        super(Klass, self).__setattr__(key, value)

    def __delattr__(self, item):
        print(f'** Called __delattr__({item!r}) method **')
        if item in self.__dict__:
            super().__delattr__(item)
        else:
            print('Opps Cant found it')

    def __getitem__(self, item):
        print(f'** Called __getitem__({item!r}) method **') # a[b]=c
        try:
            return super().__getattribute__(item)
        except:
            raise AttributeError

    def __setitem__(self, key, value):
        print(f'** Called __setitem__({key!r}, {value!r}) method **')
        self.__dict__.__setitem__(key, value)
        
    def __get__(self, instance, owner):
        print(f'** Called __get__({instance!r}, {owner!r})')
        super().__get__(instance, owner)

    def __set__(self, instance, value):
        print(f'** Called __set__({instance!r}, {value!r})')
        super().__set__(instance, value)




# myclass = Klass()
# print(myclass)
# print(repr(myclass))
# print(bytes(myclass))
# # del myclass     # myclass.__del__()
#
myclass1 = Klass(1)
# myclass2 = Klass(2)
# print(myclass1 < myclass2)
# print(hash(myclass))


