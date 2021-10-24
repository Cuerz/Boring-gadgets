# -*- coding: UTF-8 -*-
import socket


def main():
    #af_inet使用ipv4,socket_stream使用tcp通信
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(("",2222))           #绑定端口
    tcp_server_socket.listen(100)               #允许连接数
    #循环为多个用户服务多次
    while True:
        #等待用户连接，保存用户的socket和ip地址
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("The %s is connecting"%(str(client_addr)))
        #给客户发送信息
        new_client_socket.send('welcome'.encode("utf-8"))
        #循环为客户服务
        while True:
            try:
                #接收客户数据
                recv_data = new_client_socket.recv(1024)
                print(recv_data.decode("utf-8"))
            except:
                print("断开连接")
                break
        #关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()


    # s = socket.socket()             #导入socket模块
    # host = '127.0.0.1'
    # #host = socket.gethostname()     #获取自己的ip地址
    # #print(host)
    # port = 1234                     #设置通信端口
    # s.bind((host,port))             #绑定ip地址和端口
    # s.listen(5)                     #等待用户连接，最多5个
    # c,addr = s.accept()             #建立和客户端的连接，c=对方的套接字，addr=对方的ip地址和连接端口以元祖形式存在
    # print("对方连接地址是",addr)
    # c.send('welcome'.encode("utf-8"))       #通过客户的套接字发送welcome给对方，utf-8编码
    # print(c.recv(1024).decode("utf-8"))     #接收客户信息
    # c.close()

    pass



if __name__ == '__main__':
    main()