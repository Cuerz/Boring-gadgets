# -*- encoding: UTF-8 -*-
import socket

def main():
    #初始化套接字，使用ipv4的udp通信
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('',6000))
    while True:
        data,addr = s.recvfrom(1024)
        print("connect by:",addr)
        print("recv data:",data.decode("utf-8"))
        s.sendto(data,addr)
    s.close()

    pass

if __name__ == '__main__':
    main()