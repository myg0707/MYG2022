"""
创建两个进程，分别复制一个文件的上半部分和下半部分，并存储到两个新的文件中，按字节大小分割文件。
"""
import os
from multiprocessing import Process
from time import sleep

# file_path = "./dict.txt"
file_path = "tttt.txt"
# file_path = "image.jpg"
file_size = os.path.getsize(file_path)


# 如果父进程创建文件对象f，两个子进程使用这个f会相互影响
# f = open(file_path, "rb")

def copy_file_top(file_path, size, copy_size):
    f = open(file_path, "rb")
    with open("top_part_" + file_path, "wb") as new_f:
        for i in range(size // 2 // copy_size):
            new_f.write(f.read(copy_size))
        if size // 2 % copy_size > 0:
            new_f.write(f.read(size // 2 % copy_size))
    f.close()


def copy_file_bot(file_path, size, copy_size):
    f = open(file_path, "rb")
    f.seek(size // 2)
    with open("bottom_part_" + file_path, "wb") as new_f:
        while True:
            data = f.read(copy_size)
            if not data:
                break
            new_f.write(data)
    f.close()


p1 = Process(target=copy_file_top, args=(file_path, file_size, 1024))
p2 = Process(target=copy_file_bot, args=(file_path, file_size, 1024))

p1.start()
p2.start()

p1.join()
p2.join()
