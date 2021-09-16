import pickle


class A:
    def __init__(self):
        self.value = 123
        self.string = 'hello'


if __name__ == "__main__":
    objectA = A()
    filename = 'class_file'
    outfile = open(filename, 'wb')  #written in binary form
    pickle.dump(objectA, outfile)
    outfile.close()
