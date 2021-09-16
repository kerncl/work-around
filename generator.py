''' Default
def square_numbers(nums):
    result = []
    for i in nums:
        result.append((i*i))
    return result
my_nums = square_numbers([1,2,3,4,5])
print (my_nums)
'''

def square_numbers(nums):
    for i in nums:
        yield i*i #generator
my_nums = square_numbers([1,2,3,4,5])
#print ("Using next() function to print the generator object")
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
print("Using for loop to print the object")
for num in my_nums:
    print(num)

my_nums_lc= [x*x for x in [1, 2, 3, 4, 5]]
print("Using list comprehnsion method")
print(list(my_nums_lc))
for num in my_nums_lc:
    print(num)
