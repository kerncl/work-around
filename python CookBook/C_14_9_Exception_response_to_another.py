def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occured ') from e


def example2():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occured ')


def nested_exception():
    try:
        int('N/A')
    except ValueError as e:
        if 'base 10' in e.__str__():
            raise
    except Exception as e:
        print(e)


if __name__ == '__main__':
    try:
        example()
    except RuntimeError as e:
        print('It didnt work:', e)
        if e.__cause__:
            print('Cause:', e.__cause__)
        if e.__context__:
            print('Context:', e.__context__)

    # nested_exception()