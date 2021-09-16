class fish():
    def nature(self):
        print ('can swim')

class bird():
    def nature(self):
        print ('can fly')

class lizard():
    def nature(self):
        print ('can crawl')

class Human():
    def nature(self):
        print ('can do all')

def nature(name):
    name.nature()

a=fish()
b=bird()
c=lizard()
d=Human()

nature(a)
nature(b)
nature(c)
nature(d)
