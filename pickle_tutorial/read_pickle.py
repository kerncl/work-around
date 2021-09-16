import pickle

filename= 'dogs'
infile = open(filename, 'rb')   #read in binary
new_dict = pickle.load(infile)
infile.close()
print(new_dict)