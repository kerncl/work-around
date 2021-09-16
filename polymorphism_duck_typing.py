class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class myeditor:
    def execute(self):
        print('Spell check')
        print('convention check')
        print ('complieing')
        print('running')

class laptop:
    def code(self,ide):
        ide.execute()       #args take in class and run the method 'execute'


ide1 = pycharm()
ide2 = myeditor()
lap1 = laptop()
lap1.code(ide1)
lap1.code(ide2)