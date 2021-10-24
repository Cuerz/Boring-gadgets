# -*- encoding: UTF-8 -*-
import socket
import os

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '10.0.173.185'
    port = 12344
    s.connect((host,port))

    while True:
        data_recv = s.recv(1024)
        print(data_recv.decode("utf-8"))
        msg = input("send msg:")
        s.send(msg.encode("utf-8"))
    s.close()

    pass

if __name__ == '__main__':
    main()