import time

import paramiko

remote = paramiko.SSHClient()
remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote.connect(hostname='<hostname>', username='id', password='pw')
stdin, stdout, stderr = remote.exec_command('pwd')
print(f'PWD: {stdout.read()}')

# Open an interactive shell
remote_live = remote.invoke_shell()
remote_live.send('pwd\n')   # Send command interactively
time.sleep(1)
o = remote_live.recv(1000)  # received stdout
print(o)

# journalctl -f
remote_live.send("journalctl -f | grep 'power-control'\n")  # send command interactively
time.sleep(10)
for retried in range(3):
    o = remote_live.recv(1000)
    print(o)

print('End')
