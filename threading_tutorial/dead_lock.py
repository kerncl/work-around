import threading


l = threading.Lock()
print("before first acquire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")

# it hang at the third "acquired lock twice"
#Solution: with context manager