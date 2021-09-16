class Person:
    def __init__(self, name):
        self.name = name

    #Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError('Cant delete attribute')


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPerson2(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name()


# A descriptor
class String:
    # def __init__(self, name):
    #     self.name = name

    def __set_name__(self, owner, name):
        print(f'called __set_name__ ({owner!r}, {name!r})')
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


# A class with a descriptor
class Person2:
    name = String()

    def __init__(self, name):
        self.name = name


# Extending a descriptor with property
class SubPerson3(Person2):

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson3, SubPerson3).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson3, SubPerson3).name.__delete__(self)


if __name__ == '__main__':
    s = SubPerson('Guido')
    s = SubPerson2('Larry')