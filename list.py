earth_metal = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
earth_metal.sort(reverse=True)
print(earth_metal)

# Sort(key=none, reverse=False) ** list **
# key: function
Planets = [
    ('Mercuy', 2440, 5.43, 0.395),
    ('Venus', 6052, 5.24, 0.723),
    ('Earth', 6378, 5.52, 1.000),
    ('Mars', 3396, 3.93, 1.530),
    ('Jupiter', 71492, 1.33, 5.210),
    ('Saturan', 25559, 1.27, 19.213),
    ('Uranus', 25559, 1.27, 19.213),
    ('Neptune', 24764, 1.64, 30.070)
]
size = lambda planet: planet[1]
Planets.sort(key=size, reverse=True)
print(Planets)

density = lambda planet: planet[2]
Planets.sort(key=density)
print(Planets)

# Sorted  ** tuples **
data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print(sorted(data))