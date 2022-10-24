from typing import List, Dict, Union, Iterable
import json


a = {'access_methods': ['SMN'],
     'instance_name': '_instCMP0',
     'register_def': {'access_right': 0,
                      'description': None,
                      'fields': [{'end_bit': 63,
                                  'field_values': None,
                                  'name': 'Reserved_63_56',
                                  'reset': 0,
                                  'start_bit': 56,
                                  'visibility': 0},
                                 {'end_bit': 55,
                                  'field_values': None,
                                  'name': 'ErrorAddr',
                                  'reset': 0,
                                  'start_bit': 0,
                                  'visibility': 0}],
                      'ip_id': 165,
                      'ip_name': 'MCA_CS',
                      'name': 'MCA_ADDR_CS',
                      'offset': 0,
                      'phymnemonic': None,
                      'reset': "64'b0000000000000000000000000000000000000000000000000000000000000000",
                      'response_description': None,
                      'title': None,
                      'visibility': 0,
                      'volatile': None,
                      'width': 64}
     }


class Dict_Node:
    def __init__(self, data: Union[Dict, List]):
        self.data = data

    def __getattr__(self, item):
        if item not in self.data:
            raise RuntimeError(f"Key: {item} not found")

        val = self.data[item]

        if isinstance(val, int) or isinstance(val, str):
            return val

        if isinstance(val, list):
            new_list = []
            for i in val:
                new_list.append(Dict_Node(i))
            return new_list

        if isinstance(val, dict):
            return Dict_Node(val)

    def __getitem__(self, item):
        return getattr(self, item)

    def __dir__(self) -> Iterable[str]:
        return [_ for _ in self.data.keys()]

    def __repr__(self):
        return json.dumps(self.data, indent=4)


if __name__ == '__main__':
    a = Dict_Node(a)
    print(a.access_methods)
    print(a.register_def.access_right)
    print(a.register_def.fields[0])
    print(type(a.register_def.fields[0]))