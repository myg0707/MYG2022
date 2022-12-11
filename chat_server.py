"""
chat room server
env:python3.10
socket udp & fork
"""
from socket import *
import os, sys

"""
全局变量：很多封装模块都要用或者有一定的固定含义
"""
# 服务器地址
ADDR = ("192.168.74.133", 8888)
# 存储用户
user = {}


# 登录
def do_login(s, name, addr):
    if name in user:
        s.sendto("该用户存在".encode(), addr)
        return
    s.sendto("OK".encode(), addr)
    # 通知其他人
    msg = "欢迎'%s'进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr


# 聊天
def do_chat(s, name, text):
    msg = "%s:%s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


# 退出
def do_quit(s, name):
    msg = "%s退出聊天室" % name
    for i in user:
        if i == name:
            s.sendto("EXIT".encode(), user[i])
        else:
            s.sendto(msg.encode(), user[i])
    del user[name]


# 处理请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(4096)
        tmp = data.decode().split(" ")  # 拆分请求
        # 根据不同的请求类型执行不同的事情
        # L进入   C聊天     Q退出
        if tmp[0] == "L":
            do_login(s, tmp[1], addr)  # 执行具体工作
        elif tmp[0] == "C":
            text = " ".join(tmp[2:])
            do_chat(s, tmp[1], text)
        elif tmp[0] == "Q":
            do_quit(s, tmp[1])
        else:
            pass


# 搭建网络
def main():
    # udp 服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:  # 子进程处理管理员消息
        while True:
            msg = input("管理员消息：")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(), ADDR)

    # 请求处理函数
    do_request(s)


main()
