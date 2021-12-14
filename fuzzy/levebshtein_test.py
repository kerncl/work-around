import Levenshtein as lev


str1 = 'Apple Inc.'
str2 = 'apple Inc'


distance = lev.distance(str1.lower(), str2.lower())
print(distance)

ratio = lev.ratio(str1.lower(), str2.lower())
print(ratio)