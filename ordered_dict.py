#Dictionary
#dictionary will follow the has number
scores = [('Nukhil',6), ('Rohan',7), ('Manish',8), ('Ram',10)]
d = {}
for name, score in scores:
    d[name]=score

print(d)
print(d.keys())
print(d.values())

#Ordered Dictionary
#ordered dictionry will follow the user sequence
from collections import OrderedDict
odict = OrderedDict(scores)
print(odict)
print(odict.keys())
print(odict.values())
