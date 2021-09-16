class Klass():
    class_var_a = 'abc'

    def __init__(self, value=''):
        self.class_var_a = value

    def A(self):
        print('method A')
        self.instance_var_a = 'bcd'
        self.class_var_a = 'I have changed... class var????'
        Klass.B()


    @staticmethod
    def B():
        print('method B')



    @classmethod
    def C(cls):
        print('method C')
        cls.class_var_a = 'class_var_a changed using C'
        return cls()

    @classmethod
    def from_mp3(cls):
        print('method D')
        cls.class_var_a = 'class_var_a changed using D'
        return cls()


if __name__ == '__main__':
    Klass.B()

    inst_A = Klass('C_wengheng')
    inst_A.A()
    inst_A.class_var_a = '!!!!'
    print(inst_A.class_var_a)
    print(f'*** {Klass.class_var_a}')

    inst_B = Klass('D_wengheng')
    inst_B.A()
    inst_B.class_var_a = '###'
    print(inst_B.class_var_a)
    print(f'*** {Klass.class_var_a}')

    inst_C = Klass()
    inst_C.A()
    inst_C.class_var_a = '%%%%%%'
    print(inst_C.class_var_a)
    print(f'*** {Klass.class_var_a}')



    # instan_using_D = Klass.D()
    # print(instan_using_D.class_var_a)
    # myinst = Klass()
    # print(myinst.class_var_a)
    #
    # instan_using_C = Klass.C()
    # print(instan_using_C.class_var_a)
    # print(f'*** {Klass.class_var_a}')
    #
    # myinst = Klass()
    # print(myinst.class_var_a)

