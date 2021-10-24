# -*- encoding: UTF-8 -*-
import socket

def send_file_2_client(new_client_socket,client_addr):
    #客户端要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端 %s 要下载 %s"%(str(client_addr),file_name))
    #按照客户端的要求读取文件
    file_content = None
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as e:
        print("没有要下载的文件%s"%(file_name))
    #读取出文件并发送
    if file_content:
        new_client_socket.send(file_content)

def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(("",1234))
    tcp_server_socket.listen(100)
    while True:
        new_client_socket,client_addr = tcp_server_socket.accept()
        #调用发送文件的函数
        send_file_2_client(new_client_socket,client_addr)
        new_client_socket.close()
    tcp_server_socket.close()

    pass

if __name__ == '__main__':
    main()