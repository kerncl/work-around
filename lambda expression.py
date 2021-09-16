# Lambda Expression
# lambda input_value1 input_value2 ... : operation

# Example 1:
g = lambda x: 3*x+1
print(g(2))

# Example 2:
full_name = lambda fn, ln : fn.strip().title() + " " + ln.strip().title()
print(full_name('Chin', 'Linn Kern'))

# Example 3:
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Rober Heinlein', 'Arthur C. Clarker', 'Frank Herbert']
scifi_authors.sort(key= lambda name: name.split(" ")[-1].lower())
print(scifi_authors)


# Example 4:
def quadratic_function(a, b, c):
    '''Return the function f(x)=ax^2+ bx + c'''
    return lambda x: a*x**2 + b*x + c


f = quadratic_function(3, 0, 1)
print(f(2))
print(quadratic_function(3, 0, 1)(2)) # Equivalent with on top

# Map function
# Example 1:
import math
def area(r):
    ''' Area of a circle with radius 'r' '''
    return math.pi* (r**2)
radii = [2, 5, 7.1, 0.3, 10]
# Method 1: Direct Method
areas_1 = []
for r in radii:
    a = area(r)
    areas_1.append(a)
print('Direct Method:' + str(areas_1))

# Method 2: Map Method:  map(function, iteration)
areas_2 = list(map(area, radii)) # map return an object; object --> list
print('Map Method: '+ str((areas_2)))

# Example 2:
temps = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Lost Angles', 26), ('Tokyo', 27), ('New York', 28), ('London', 22), ('Bejing', 32)]
c_to_F = lambda data: (data[0], (9/5)*data[1] + 32) # Passing a tuples or list into lambda function
print(str(list(map(c_to_F, temps))))


# Filter Function:  filter(object to filter, iteration)
# Example 1:
import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print('Above avg: ' + str(list(filter(lambda x: x > avg, data))))
print('Below avg: ' + str(list(filter(lambda x: x < avg, data))))

# Example 2: #remove missing data
countries = ['', 'Agentina', " ", 'Brazil', 'Chile', '', 'Colombia', 0, ()]
print(str(list(filter(None, countries))))

# Reduce Function:
data1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Method 1: Direct Method
product = 1
for x in data:
    product = product * x
print('Direct Method', product)
# Method 2: Reduce Function
from functools import reduce
mult = lambda x, y: x*y
print('Reduce Method:', reduce(mult, data))

