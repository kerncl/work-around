def lower_case(func):
    def wrapper_lower_case(*args):
        # value = args[0]
        # func(value.lower())
        func(args[0].lower())
    return wrapper_lower_case

@lower_case
def print_func(text):
    print(text)
# print_func = lower_case(print_func)

if __name__ == '__main__':
    print_func('abc')
    print_func('ABC')