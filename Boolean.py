#Boolean values: True, False
###Value
#True
print(bool(True))
print(bool(1))
print(bool(2.232))
print(bool(-12312.231))
#False
print(bool(0))

###String
#True
print(bool("abc"))
print(bool(" "))
#False
print(bool(""))

# List, Dictionary, Tuple
list = []
dic = {}
tupl = ()
print(bool(list))
print(bool(dic))
print(bool(tupl))