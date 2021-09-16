from example_module import hello_class

print('Say hi from import_module file')

if __name__ == '__main__':
    print('start')
    print('going to call hello method inside hello_class')
    a = hello_class()
    print('done initial hello class')
    a.hello()
    from example_module import hello_class