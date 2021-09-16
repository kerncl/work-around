import pickle
from pickle_tutorial.write_class_pickle import A

filename= 'class_file'
infile = open(filename, 'rb')   #read in binary
new_class = pickle.load(infile)
infile.close()
print(new_class)