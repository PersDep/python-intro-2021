import random
from time import sleep
import asyncio
import time

import warnings
warnings.filterwarnings("ignore")

n = 50000000
constn = n

def countdown(k):
    global n
    for _ in range(k):
        n -= 1
    sleep(0.1)
    print('Subtracted %s' % k)

async def asyncountdown(k):
    global n
    async with sem:
        for _ in range(k):
            n -= 1
    await asyncio.sleep(random.randint(0, 2) * 0.2)
    # await asyncio.sleep(0.1)
    print('Subtracted %s' % k)

def task(pid):
    """Synchronous non-deterministic task.
    """
    sleep(0.2) # random.randint(0, 2) *
    print('Task %s done' % pid)


async def task_coro(pid):
    """Coroutine non-deterministic task
    """
    await asyncio.sleep(0.2)
    print('Task %s done' % pid)


def synchronous():
    for i in range(10):
        countdown(constn // 10 - i)


async def asynchronous():
    tasks = [asyncio.ensure_future(asyncountdown(constn // 10 - i)) for i in range(10)]
    await asyncio.wait(tasks)

print(n)

print('Synchronous:')
start = time.time()
synchronous()
print(time.time() - start)

print(n)
n = 50000000

ioloop = asyncio.get_event_loop()
sem = asyncio.Semaphore(constn)
print('Asynchronous:')
start = time.time()
ioloop.run_until_complete(asynchronous())
ioloop.close()
print(time.time() - start)

print(n)
