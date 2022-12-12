"""github 修改内容
multiprocessing 模块创建进程
1. 编写进程函数
2. 产生进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
from time import sleep

a = 1


def fun():
    print("开始一个进程")
    sleep(2)
    global a
    a = 10000
    print("a = ", a)
    print("子进程结束")


# 创建进程对象
p = mp.Process(target=fun)
p.start()  # 启动进程

# 父进程时间
sleep(3)
print("父进程干点事")

p.join()  # 回收进程

print("a:", a)
"""
pid = os.fork()
if pid == 0:
    fun()
    os._exit(0)
else:
    os.wait()
"""
