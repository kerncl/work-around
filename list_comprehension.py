# List Comprehension
#Example 1: [expr for val in collection]
#Example 2: [expr for val in collection if <test>]
#Example 3: [expr for val in collection if <test1> and <test2>]
#Example 4: [exprt for val in collection1 and val2 in collectiono2]

squares = []
for i in range(1,101):
    squares.append(i**2)
print("Default Coding")
print(squares)
#Example 1:
squares_list = [i**2 for i in range(1, 101)]
print("List Comprehension Example 1:")
print(squares_list)
#Example 1.1:
remainders5 = [x**2 % 5 for x in range(1,101)]
print("Remainders of 5")
print(remainders5)
#Example 2:
movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the Wind", "Citizen Kane"]
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
print("Default Example 2")
print(gmovies)
gmovies_list = [title for title in gmovies if title.startswith("G")]
print("List Comprehension Example 2:")
print(gmovies_list)
#Example 3:
movies_dic = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It is a wonderful Life", 1946), ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954)]
movies_dic_list = [title for (title, year) in movies_dic if year > 2000]
print((movies_dic_list))
#Example 4:
v = [2, -3, 1]
w = [4*x for x in v]
print("Scalar Example 4:")
print(w)
#Example 5:
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a,b) for a in A for b in B]
print("Example 5:")
print(cartesian_product)
#Example 6:
cartesian_product2 = [(a,b) for a,b in zip(A,B)]   #combine two list into tuples
print("Example 6:")
print(cartesian_product2)


