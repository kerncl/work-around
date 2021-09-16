import pickle
import bz2
dogs_dict = {'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}
filename = 'dogs'

#Write into pickle
outfile = open(filename, 'wb')  #written in binary form
sfile = bz2.BZ2File(filename+'bz2', 'wb')
pickle.dump(dogs_dict, outfile)
pickle.dump(dogs_dict, sfile)
outfile.close()

#Read from pickle
infile = open(filename, 'rb')   #read in binary
new_dict = pickle.load(infile)
infile.close()

#Validate
print(dogs_dict==new_dict)
print(f'Dogs_dict : Type {type(dogs_dict)}')
print(f'New_dict : Type {type(new_dict)}')