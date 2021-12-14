from fuzzywuzzy import fuzz

print('Test 1')
str1 = 'Apple Inc.'
str2 = 'apple Inc'
print(f'str1: {str1}\n str2: {str2}')

ratio = fuzz.ratio(str1.lower(), str2.lower())
print(f'Ratio: {ratio}')
print()


print('Test 2')
str1 = 'Los Angeles Lakers'
str2 = 'Lakers'
print(f'str1: {str1}\n str2: {str2}')

ratio = fuzz.ratio(str1.lower(), str2.lower())
partial_ratio = fuzz.partial_ratio(str1.lower(), str2.lower())
print(f'Ratio: {ratio}')
print(f'Partial Ratio: {partial_ratio}')
print()


print('Test 3')
str1 = 'united states v. nixon'
str2 = 'Nixon v. United States'
print(f'str1: {str1}\n str2: {str2}')

ratio = fuzz.partial_ratio(str1.lower(), str2.lower())
partial_ratio = fuzz.token_set_ratio(str1, str2)
token_sort_ratio = fuzz.token_set_ratio(str1.lower(), str2.lower())
print(f'Ratio: {ratio}')
print(f'Partial Ratio: {partial_ratio}')
print(f'Token Sort Ratio: {token_sort_ratio}')
print()

print('Test 4')
str1 = 'The supreme court case of Nixon vs The United States'
str2 = 'Nixon v. United States'
print(f'str1: {str1}\n str2: {str2}')

ratio = fuzz.ratio(str1.lower(), str2.lower())
partial_ratio = fuzz.partial_ratio(str1.lower(), str2.lower())
token_sort_ratio = fuzz.token_set_ratio(str1, str2)
token_set_ratio = fuzz.token_set_ratio(str1, str2)
print(f'Ratio: {ratio}')
print(f'Partial Ratio: {partial_ratio}')
print(f'Token Sort Ratio: {token_sort_ratio}')
print(f'Token Set Ratio: {token_set_ratio}')
print()


from fuzzywuzzy import process
str2match = 'apple inc'
stroptions = ['apple inc.', 'apple park', 'apple incorporated', 'iphone']
ratio = process.extract(str2match, stroptions)
print(f'Ratio: {ratio}')

highest = process.extractOne(str2match, stroptions)
print(f'Highest: {highest}')