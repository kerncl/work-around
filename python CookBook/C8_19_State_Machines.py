class State:
    def __init__(self):
        self.new_state(State_A)

    def new_state(self, state):
        self.__class__ = state

    def action(self, x):
        raise NotImplemented()


class State_A(State):
    def action(self, x):
        print(f'Doing Action in A {x}')
        self.new_state(State_B)

    def actionA(self):
        print(f'Special Action in A')


class State_B(State):
    def action(self, x):
        print(f'Doing Action in B {x}')
        self.new_state(State_C)

    def actionB(self):
        print(f'Special Action in B')


class State_C(State):
    def action(self, x):
        print(f'Doing Action in C {x}')
        self.new_state(State_A)

    def actionC(self):
        print(f'Special Action in C')


state = State()