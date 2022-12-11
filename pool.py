"""
pool 进程池使用事例
"""

from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件
def worker(msg):
    sleep(2)
    print(ctime(), "--", msg)


# 创建进程池,注意事件函数要写在进程池上方
pool = Pool(4)

# 向进程池队列添加事件
for i in range(10):
    msg = "Tedu %d" % i
    pool.apply_async(func=worker, args=(msg,))

# 关闭进程池
pool.close()
# 回收进程池
pool.join()
