def A():
    global G
    G=10
    print('A:', G)

def B():
    G=5
    print('B:', G)

def C():
    print('G:', G)
if __name__ == "__main__":
    G=1
    print('G:', G)
    B()
    A()
    B()
    C()
    B()