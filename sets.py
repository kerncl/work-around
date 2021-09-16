example = set()
example.add(42)
example.add(False)
example.add(3.142)
example.add("Thorium")
len(example)
example.remove(42)

#2 way to remove from set
#example.remove(1) #flag error if doesnt exist
#example.discard(1) #wont flag error if doesnt exist
#example.clear() #remove all value from set

# Intercept
odds= set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
prime_number = set([2, 3, 5, 7])
composites = set ([4, 6, 8, 9, 10])

odds.union(evens)
evens.union(odds)
odds.intersection(prime_number)
prime_number.intersection(evens)
evens.intersection(odds)

#Check value in sets , return bool
2 in prime_number
6 in odds