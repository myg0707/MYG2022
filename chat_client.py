"""
chat room client
发送请求，展示结果
"""
from socket import *
import os, sys
import signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 服务器地址
ADDR = ("192.168.74.133", 8888)


def msg_send(s, name):
    while True:
        try:
            text = input("消息：")
        except KeyboardInterrupt:
            text = "quit"
        if text.strip() == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


def msg_recv(s):
    while True:
        try:
            data, addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + "\n消息：", end="")


# 客户端启动函数
def main():
    s = socket(AF_INET, SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入姓名：")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 接收反馈
        data, addr = s.recvfrom(128)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    # 聊天
    pid = os.fork()
    if pid < 0:
        print("Error")
    elif pid == 0:
        msg_recv(s)
    else:
        msg_send(s, name)


main()
