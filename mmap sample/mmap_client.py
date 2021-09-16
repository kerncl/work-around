import mmap


class Protected_file:
    def __init__(self, file):
        self.file = file


class mmap_context:

    def __new__(cls, file):
        instance = Protected_file(file)
        instance.__class__ = cls
        return instance

    def __enter__(self):
        self.__mm = mmap.mmap(fileno=self.file.fileno(), length=1024, access=mmap.ACCESS_READ)
        return self.__mm

    def __exit__(self, *args, **kwargs):
        self.__mm.close()

    def __setattr__(self, key, value):
        if key == self.file:
            raise AttributeError('Sorry Children dont try to change the file going to READ SOON !!')
        super().__setattr__(key, value)


with open('data.dat', 'r') as f:
    with mmap_context(f) as mem:
        print(mem.read())
