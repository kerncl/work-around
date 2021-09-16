import threading
import time
import concurrent.futures

def do_something(sec):
    print(f'Sleeping {sec} second ...')
    time.sleep(sec)
    return 'Done Sleeping {}s...'.format(sec)


start = time.perf_counter()
# Example 1: Traditional Threading method
#threads = []
#for _ in range(10):
#    t=threading.Thread(target=do_something)
#    t.start()
#    threads.append(t)
#
#for thread in threads:
#    thread.join()

# Example 2:
secs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Option 1:
    #f1 = executor.submit(do_something, 1)
    #f2 = executor.submit(do_something, 3)
    #print(f1.result())  # run until result complete
    # print(f2.result())  # run until result complete
    #Option 2: List comprehensive
    #results = [executor.submit(do_something, sec) for sec in range(len(secs)+1)]
    #for f in concurrent.futures.as_completed(results):
    #    print(f.result())
    #Option 3: using Map method
    results = executor.map(do_something, secs)
    for result in results:
        print(result)
finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')
