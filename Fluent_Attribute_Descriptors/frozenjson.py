from collections import abc
import json
import os


class FrozenJSON:
    """
        A read-only facade for navigating a JSON-like object using attribute notation
    """

    def __int__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJSON.build(self.__data[item])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == '__main__':
    JSON = os.path.join(os.path.dirname(__file__), 'osconfeed.json')
    with open(JSON) as fp:
        json_dict = json.load(fp)
    feed = FrozenJSON(json_dict)
    print(len(feed.Schedule.keys()))
    print(sorted(feed.Schedule.keys()))
    print(feed.Schedule.speakers[-1].name)
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    print(talk.flavor)


