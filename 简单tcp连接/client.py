# -*- coding: UTF-8 -*-
import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_ip = '127.0.0.1'
    server_port = 2222
    server_add = (server_ip,server_port)
    #连接服务器
    tcp_socket.connect(server_add)
    #接收第一次发来的数据
    first_data = tcp_socket.recv(1024)
    print(first_data.decode("utf-8"))
    while True:
        send_data = input("send-->")
        tcp_socket.send(send_data.encode("utf-8"))
    tcp_socket.close()
    # s = socket.socket()
    # host = '127.0.0.1'                       #要连接的ip地址
    # port = 1234                             #目标端口
    # s.connect((host,port))                  #连接服务端
    # print(s.recv(1024).decode("utf-8"))     #接收信息
    # msg = input("message:")
    # s.send(msg.encode("utf-8"))     #发送信息
    # s.close()

    pass



if __name__ == '__main__':
    main()