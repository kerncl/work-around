
class Klass:
    """my Klass"""

class Klass_foo(Klass):
    """foo Klass"""
    var_a = 1
inst_a = Klass()
inst_b =  Klass()

print(hex(id(Klass)))
print(hex(id(inst_a)))
print(hex(id(inst_b)))


foo_inst = Klass_foo()
pass