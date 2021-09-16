import sys
import timeit
#Lists []
prime_number = [2, 3, 5, 7, 11, 13, 17]
print('#Primes =',len(prime_number))
for p in prime_number:
    print("Prime", p)
print(dir(prime_number))  #lists has more standard built in method than tuple such as add, remove, discard
print("List size memory:", sys.getsizeof(prime_number)) #List has larger memory than tuple
list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
print("List time", list_test)
#Tuples ()
perfect_number = (1, 4, 9, 16, 25, 36)
print('# Squares =', len(perfect_number))
for n in perfect_number:
    print('#Perfect number', n)
print(dir(perfect_number))
print('Tuples size of memeory:', sys.getsizeof(perfect_number)) #Tuple has least memory then list
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
print("Tuple time", tuple_test)
#Example 1:
empty_tuple = ()
test1= ('a') #string
test1_t = ('a',) #tuple ; test1_t = a,
test2= ('a', 'b') #test2= a, b
test3= ('a', 'b', 'c') #test3 = a,b,c
print(empty_tuple)
print(test1)
print(test1_t)
print(test2)
print(test3)

#Example 2:
#(age, country, knows_python)
survey = 27, 'country', True
age = survey[0]
country = survey[1]
knows_python = survey[2]
print('Age=',age)
print('Country=', country)
print('knows_python=', knows_python)
survey2 = 21, 'SwitzerLand', False
age, country, knows_python = survey2 # the number of variable need to be same as the len of tuples
print('Age=',age)
print('Country=', country)
print('knows_python=', knows_python)