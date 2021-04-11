#!/usr/bin/env python3

from multiprocessing import Manager, Pool, Queue, Process
import os
import time
import random
import signal
import itertools


def dispatcher(task, req):
    print(f"dispatcher start")
    for t in task:
        try:
            req.put(t)
            print(f"dispatcher put new task: {t}")
        except:
            print(f"dispatcher break")
            break
    print(f"dispatcher exit")


def worker(req, res):
    pid = os.getpid()
    print(f"worker {pid} start")
    while True:
        try:
            t = req.get()
            print(f"worker {pid} get task: {t}")
            time.sleep(random.randint(1, 4))  # hardworking
            res.put(t)
            print(f"worker {pid} done task: {t}")
        except:
            print(f"worker {pid} break")
            break
    print(f"worker {pid} exit")


def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def loop():
    cpus = os.cpu_count()
    task = itertools.count()  # infinite counting

    mgr = Manager()
    req = mgr.Queue(cpus)
    res = mgr.Queue(cpus)

    disp = Process(target=dispatcher, args=(task, req))
    disp.start()

    pool = Pool(cpus, initializer=init_worker)
    for _ in range(cpus):
        pool.apply_async(worker, args=(req, res))

    # quit by CTRL+C
    def int_handler(n, f):
        print(f"signal {n} received, quit")
        mgr.shutdown()
    signal.signal(signal.SIGINT, int_handler)

    while True:
        try:
            r = res.get()
            print(f"got result: {r}")
        except:
            print(f"main loop break")
            break

    disp.join()
    pool.close()
    pool.join()


if __name__ == '__main__':
    loop()
