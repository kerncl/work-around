import subprocess
p1 = subprocess.run('dir', shell=True )
#capture_output=True, text=True)

print(p1.args) # print the input command
print(p1.returncode) # return status of code
print(p1.stdout) # print output result
print(p1.stderr) #print error

# write into file
#with open('output.txt', 'w') as f:
#    p2 = subprocess.run('type subprocesss.py', shell=True, stdout=f, text=True)
