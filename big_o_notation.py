import time

start_time = time.time()
n = 100000
for x in range(n):
    time.sleep(0.001)
    time.sleep(0.001)
    time.sleep(0.001)

total_time = time.time() - start_time
print(total_time)

start_time = time.time()

for x in range(n):
    time.sleep(0.001)

for x in range(n):
    time.sleep(0.001)

for x in range(n):
    time.sleep(0.001)

total_time = time.time() - start_time
print(total_time)


