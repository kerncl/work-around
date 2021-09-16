def generator_func(value):
    if not value%2:
        print('Generator func: it is an Even number')
        yield 'Even'
    if not value%3:
        print('Generator func: it is an Odd Number')
        yield 'Odd'

for value in [1,2,3,4,5,6,7,8,9,10]:
    status = generator_func(value)
    print(status)
