## INPUT ###
list_1 = [{'primary_key1': 'primary_key_value1',
           'item1': ['list1',
                     'list4'],
           'item2': 'str',
           'item3':
               [{'primary_child_key1': 'primary_child_key_value1',
                 'itemchild1': 'str',
                 'itemchild2': 'str',
                 'itemchild3': 'str',
                 'itemchild4': 'str',
                 'itemchild5': [
                     'itemlistchild1'
                 ]},
                {'primary_child_key1': 'primary_child_key_value2',
                 'itemchild1': 'str',
                 'itemchild2': 'str',
                 'itemchild3': 'str',
                 'itemchild4': 'str',
                 'itemchild5': [
                     'itemlistchild1'
                 ]},
            ]
           }]
list_2 = [{'primary_key1': 'primary_key_value1',
           'item1': ['list1',
                     'list2',
                     'list3'],
           'item2': 'str',
           'item3': [{'primary_child_key1': 'primary_child_key_value1',
                      'itemchild1': 'str',
                      'itemchild2': 'str',
                      'itemchild3': 'str',
                      'itemchild4': 'str',
                      'itemchild5': [
                                    'itemlistchild2'
                        ]},
                     {'primary_child_key1': 'primary_child_key_value2',
                      'itemchild1': 'str',
                      'itemchild2': 'str',
                      'itemchild3': 'str',
                      'itemchild4': 'str',
                      'itemchild5': [
                                    'itemlistchild2'
                        ]},
                    ]
           }]

from collections import UserList, UserDict, MutableSequence, defaultdict, OrderedDict, MutableMapping
from pprint import pprint


class CustomDict(UserDict):
    def __init__(self, mapping: OrderedDict):
        self.data = OrderedDict()
        for key, value in mapping.items():
            if isinstance(value, MutableSequence):
                # Data Type : List
                if len(value):
                    if isinstance(value[-1], MutableMapping):
                        # Child Value is a Dict
                        self.data.update({key: CustomList(value)})
                    else:
                        # String type
                        self.data.update({key: set()})
                        self.data[key].update(value)
                else:
                    # Empty List
                    self.data.update({key: set()})
            else:
                # String Type
                self.data.update({key: value})

    def update(self, mapping, **kwargs) -> None:
        for key, value in mapping.items():
            if isinstance(value, MutableSequence):
                # List
                self.data[key].update(value)


class CustomList(UserList):
    def __init__(self, initlists=None):
        self.data = []
        for initlist in initlists:
            self.data.append(CustomDict(initlist))

    def append(self, item: OrderedDict) -> None:
        if not len(item):
            return
        self._dict_key = [_ for _ in item][0]
        if item.get(self._dict_key) in self:
            signature = item.get(self._dict_key)
            self[signature].update(item)
        else:
            self.data.append(item)

    def extend(self, other) -> None:
        for item in other:
            self.append(item)

    def index(self, item, *args):
        for i, _ in enumerate(self):
            if item == _.get(self._dict_key):
                return i

    def __contains__(self, item):
        return item in [_.get(self._dict_key) for _ in self]

    def __iter__(self):
        for dict_data in self.data:
            yield dict_data

    def __getitem__(self, item):
        for _ in self:
            if _.get(self._dict_key) == item:
                return _
        raise KeyError(f'{item} not Found')

    def update(self, items_list: MutableSequence):
        for item in items_list:
            self.append(OrderedDict(item))

    def to_json(self):
        return_data = OrderedDict()
        for dict_data in self:
            for key, value in dict_data.items():
                pass


if __name__ == '__main__':
    # Case 1: Manual Insert
    sig_a = OrderedDict(list_1[-1])
    sig_b = OrderedDict(list_2[-1])
    mydict1 = CustomDict(sig_a)
    pprint(mydict1)
    mydict1.update(sig_b)
    pprint(mydict1)
    # Case 2:
    mydict2 = CustomList(list_1)
    pprint(mydict2)
    mydict2.append(sig_b)
    pprint(mydict2)


#################### Expected output ########################
output = [{'primary_key1': 'primary_key_value1',
           'item1': ['list1',
                     'list2',
                     'list3',
                     'list4'],
           'item2': 'str',
           'item3': [{'primary_child_key1': 'primary_child_key_value1',
                      'itemchild1': 'str',
                      'itemchild2': 'str',
                      'itemchild3': 'str',
                      'itemchild4': 'str',
                      'itemchild5': [
                                    'itemlistchild1',
                                    'itemlistchild2'
                        ]},
                     {'primary_child_key1': 'primary_child_key_value2',
                      'itemchild1': 'str',
                      'itemchild2': 'str',
                      'itemchild3': 'str',
                      'itemchild4': 'str',
                      'itemchild5': [
                                    'itemlistchild1',
                                    'itemlistchild2'
                        ]},
                    ]
}]

