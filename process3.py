"""
Process 给进程函数传参
"""

from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I am %s" % name)
        print("I am working...")


# p = Process(target=worker, args=(3, "Bob"))
# p = Process(target=worker, kwargs={"name": "Bob", "sec": 3})
p = Process(target=worker, args=(3,), kwargs={"name": "Bob"})
p.start()
p.join()
