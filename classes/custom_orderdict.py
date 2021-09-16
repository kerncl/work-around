from collections import OrderedDict
from collections.abc import MutableMapping


class CustomDict(OrderedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def ntg_here(self):
        print('hi')
        pass
    
    # def __repr__(self):
    #     super(CustomDict, self).__repr__()


if __name__ == '__main__':
    mydict = CustomDict({'name':'lala', 'age':10})
    print(mydict)
    mydict.ntg_here()
    pass