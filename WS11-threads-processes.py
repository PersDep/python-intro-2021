from multiprocessing import freeze_support
from multiprocessing import Pool
from multiprocessing import Process
from threading import Thread
import time


def countdown(n):
    while n > 0:
        n -= 1


count = 50000000

start = time.time()
countdown(count)
print(time.time() - start)

t1 = Thread(target=countdown, args=(count//2,))
t2 = Thread(target=countdown, args=(count//2,))
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time() - start)


freeze_support()

start = time.time()
pool_size = 4
args = [count // pool_size for i in range(pool_size)]
with Pool(pool_size) as p:
    p.map(countdown, args)
print(time.time() - start)

p1 = Process(target=countdown, args=(count//2,))
p2 = Process(target=countdown, args=(count//2,))
start = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
print(time.time() - start)
