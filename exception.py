# Exception
# try:
# except:
# else:
# finally: Always executed

import math
try:
    input_data = int(input('Please enter a value'))
    value = 1/input_data
except ZeroDivisionError as err:
    print('Error: ', err)
else:
    print('Result:', value)
finally:
    print('...... Program Ended .........')         #Will be executor no matter how
