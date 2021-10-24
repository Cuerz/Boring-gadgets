# -*- encoding: UTF-8 -*-
import socket

def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    dest_ip = input("服务器ip:")
    dest_port = str(input("下载端口："))
    tcp_socket.connect((dest_ip,dest_port))

    down_file_name = input("要下载的文件名：")
    #把文件名发给服务器
    tcp_socket.send(down_file_name.encode("utf-8"))
    #接收下载文件
    recv_data = tcp_socket.recv(1024*1024)
    #保存数据到文件
    with open("new_"+down_file_name,"wb") as f:
         f.write(recv_data)
    tcp_socket.close()


    pass

if __name__ =='__main__':
    main()
