import time
from multiprocessing import Pool, cpu_count


def sleep_(n):
    print(f'Going to sleep for {n} sec')
    time.sleep(n)
    print(f'Wake up from {n} sec')
    return n


def main():
    print(f'CPU Cores: {cpu_count()}')
    with Pool() as pool:
        pool.map(sleep_, range(50))


if __name__ == '__main__':
    main()
