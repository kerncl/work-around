import time
import multiprocessing

def do_something():
    print('Slping 1 seconds ....')
    time.sleep(1)
    return 'Done slping ..... '


start = time.perf_counter()
p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

p1.start()
# p2.start()
p1.join()
# p2.join()
#
#processes = []
#for _ in range(10):
#    p = multiprocessing.Process(target=do_something)
#    p.start()
#    processes.append(p)
#
#for process in processes:
#    processes.join()
#
finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
