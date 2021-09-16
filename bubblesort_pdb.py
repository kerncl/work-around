import random


def display_list(l):
    ''' Display list of integer values n by printing string of n length '''

    # Clear out screen
    print('\n'*50)
    for value in l:
        print('**'*value)
    # Pause until the user hits enter
    input('')


def bubblesort(l):
    ''' Sorts l in place and return it '''
    for passesLeft in range(len(l)-1, 0, -1):
        for index in range(passesLeft):
            if l[index] < l[index+1]:
                l[index], l[index+1] = l[index+1], l[index]
        display_list(l)
        return l


lst1 = [random.randrange(1, 50) for i in range (1,20)]
print(lst1)
input('')
import pdb; pdb.set_trace()
bubblesort(lst1)
print(lst1)

#s - stepinto
#n - next (skip)
#w - where i execute
#b <no.> - located the breakpoint
#c - continue run until meet breakpoint
#q - quit