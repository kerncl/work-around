import collections
import bisect

isinstance((1,), collections.Iterable)
isinstance((1,), collections.Sequence)
isinstance((1,), collections.Container)
isinstance((1,), collections.Sized)
isinstance((1,), collections.Mapping)
isinstance((1,), collections.MutableSequence)


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial else []

    def __getitem__(self, index):
        print(f'Getting: {index}')
        return self._items[index]

    def __setitem__(self, index, value):
        print(f'Setting: {index}, {value}')
        self._items[index] = value

    def __delitem__(self, index):
        print(f'Deleting {index!r}')
        del self._items[index]

    def __len__(self):
        print('Len')
        return len(self._items)

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)


if __name__ == '__main__':
    a = Items([1, 2, 3])
    print(len(a))
    a.append(4)
    print('Done append')
    a.count(2)
    print('Done count')
    a.remove(3)
