import rpyc

port_number = 19961
PIE_IP = '192.168.0.104'



def foofunc():
    return "foo"


conn = rpyc.connect(PIE_IP,port=port_number)
foo = conn.root.bar(foofunc)
print(foo)