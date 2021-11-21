import json
import string
from typing import Optional, List, Callable, MutableMapping
from collections import UserList
from functools import wraps
from pprint import pprint

import pydantic


def wrapper_print_args(func: Callable):
    """
    A wrapper function that print func argument
    Args:
        func: callable object

    Returns:
        wrapper
    """
    @wraps(func)
    def wrapper(*args: List, **kwargs: MutableMapping):
        print(f'{func.__name__}({args !r})')
        return func(*args, **kwargs)
    return wrapper


class CustomException(Exception):
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'[{self.value}]: {self.message}'


class ExceptionStrWithoutSpace(CustomException):
    pass


class ExceptionISBN10FormatError(CustomException):
    pass


class Author(pydantic.BaseModel):
    """
    Custom Dict like classes object
    """
    name: str
    verified: bool
    pass


class MyJson(pydantic.BaseModel):
    """
    Custom Json class that able to validate data
    """
    title: str
    subtitle: Optional[str]
    author: str
    publisher: str
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    price: float
    author2: Optional[Author]

    @pydantic.validator('title', 'subtitle', 'author', 'publisher', allow_reuse=True)
    # @wrapper_print_args
    @classmethod
    def validate_str_with_space(cls, v, values, **kwargs):
        """
        Validate on str datatyoe
        Args:
            v (Any): current field value
            values (Dict): Dict of field name with v
            **kwargs:

        Returns:
            v: current value
        """
        print(f'** validate_str_with_space(v={v !r}, values={values !r}, kwargs={kwargs}) **')
        if ' ' not in v:
            raise ExceptionStrWithoutSpace(value=values['title'], message=f'{v} doesnt contain space')
        return v

    @pydantic.validator('isbn_10', allow_reuse=True)
    # @wrapper_print_args
    @classmethod
    def validate_isbn10(cls, v, values, **kwargs):
        """
        Validate on int
        Args:
            v(int): current field value
            values: Dict of field name with v
            **kwargs:

        Returns:
            v: current value
        """
        print(f'** validate_isbn10(v={v !r}, values={values !r}, kwargs={kwargs}) **')
        if len(v) != 10:
            raise ExceptionISBN10FormatError(value=v, message='Document should be 10 digits')
        try:
            return int(v)
        except ValueError as e:
            raise ExceptionISBN10FormatError(value=v, message=str(e))


    @pydantic.root_validator(pre=True, allow_reuse=True) # before validator
    # @wrapper_print_args
    @classmethod
    def before_root_validator(cls, values):
        """
        Validate all field before entering root validator
        Args:
            values(dict): Dict of field name with v

        Returns:
            values(dict)
        """
        print(f'** before_root_validator(values={values !r}) **')
        return values

    @pydantic.root_validator(allow_reuse=True)
    # @wrapper_print_args
    @classmethod
    def before_validator(cls, values):
        """
        Validate all field before entering each field validator
        Args:
            values(dict): Dict of field name with v

        Returns:
            values(dict)
        """
        print(f'** before_validator(values={values !r}) **')
        return values

    def __str__(self):
        return str(self.dict())


class CustomList(UserList):
    def __init__(self, list_data):
        self.data = []
        for i, data in enumerate(list_data):
            print(f'INDEX: {i}')
            self.data.append(MyJson(**data))

    def __iter__(self):
        for _ in self.data:
            yield _

    def __str__(self):
        return ''.join(str(_) for _ in self)



if __name__ == '__main__':
    print('START')
    with open('data.json', 'r') as f:
        data = json.load(f)
        mydata = CustomList(data)
    print('DONE')
    pprint(mydata)
