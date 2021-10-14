from collections import UserDict
from copy import deepcopy

_cfg_ref = {
    'General':
        {'Goption1': 1,
         'Goption2': 2,
         'Goption3': 3},
    'Register':
        {'Roption1': 1,
         'Roption2': 2,
         'Roption3': 3},
    'Eventlog':
        {'Eoption1': 1}
}


class Option(UserDict):

    def __init__(self, *args, **kwargs):
        super().__init__()
        for dic in args:
            for key, value in dic.items():
                self.data[key] = value
        for key, value in kwargs.items():
            self.data[key] = value
            # self[key]=value


class Config(UserDict):
    _instance = None

    def __new__(cls, *args, **kwargs):  # singleton
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.data = deepcopy(_cfg_ref)
            # for section, options in _cfg_ref.items():
            #     cls._instance.data[section] = Option(options)
        return cls._instance

    def __init__(self):
        # self.data = deepcopy(_cfg_ref)
        pass

    @classmethod
    def parser(cls):
        self = cls()
        # parser & obtain dict
        user_cfg = {
            'General':
                {'Goption1': 11,
                 'Goption2': '',
                 'Goption3': 13},
            'Register':
                {'Roption1': 11,
                 'Roption2': 12}
        }
        for section, options in deepcopy(self.data).items():
            if section not in user_cfg:
                # section not found
                print(f'debug: Removing section: {section}')
                self.pop(section)
                continue
            for option, value in options.items():
                user_value = user_cfg.get(section).get(option)
                if user_value == None:
                    # Commented out
                    print(f"Using default value for : [{section}][{option}]={value}")
                else:
                    if user_value == '':
                        # empty string
                        self[section].pop(option)
                        print(f"Warning: user insert empty for [{section}][{option}]")
                        continue
                    # os environment
                    # Validate func

    def set(self, option, value):
        for section, options in self.items():
            if option in options:
                # validate func
                self[section][option] = value
                return
        raise NotImplemented(f"Invalid option {option}")


    def show(self):
        print(self)


if __name__ == '__main__':
    Config.parser()
    mycfg = Config()
    mycfg1 = Config()
    mycfg2 = Config()
    print()
    # config1 = Config()
    # config1['odict1']['idict11'] = 'abc'
    # config1['odict1'] = 'abc'
    # config2 = Config()
    # assert config1 is config2
