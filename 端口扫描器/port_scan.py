# -*- encoding: UTF-8 -*-
import sys
import socket

#判断端口是否开放
def open(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        return True
    except Exception as e:
        print(e)
        return False

#默认扫描的函数
def scan(ip,portlist):
    for x in portlist:
        if open(ip,x):
            print("%s host %s port open"%(ip,x))
        else:
            print("%s host %s port closed"%(ip,x))

#范围扫描
def rscan(ip,s,e):
    for x in range(s,e):
        if open(ip,x):
            print("%s host %s port open" % (ip, x))
        else:
            print("%s host %s port closed" % (ip, x))

def main():
    defaultport = [135,139,445,1433,3306,3389,5944]

    str = sys.argv[1]           #获取第一个参数(ip)
    if len(sys.argv) == 2:      #如果只有一个参数
        if str[0] == '-':
            option = sys.argv[1][1:]    #查看‘-’后内容
            if option == 'version':
                print("v 1.0")
            elif option == 'help':
                print("python xxx.py [ip] [port:80,99或80-99]")
            sys.exit()
        #默认没有扫描参数 python xxx.py 127.0.0.1
        scan(sys.argv[1],defaultport)

    #参数有逗号
    elif len(sys.argv) == 3:
        if ',' in sys.argv[2]:      #python xx.py ip 80,89,99
            p = sys.argv[2]         #80,89,99
            p = p.split(',')        #['80','89','99']
            a = []
            for x in p:
                a.append(int(x))
            scan(sys.argv[1],a)
        #参数有-的情况
        elif '-' in sys.argv[2]:    #python xx.py ip 80-99
            a = sys.argv[2]         #80-99
            a = a.split('-')        #['80,'99']
            s = int(a[0])           #s=80
            e = int(a[1])           #e=99
            rscan(sys.argv[1],s,e)

    pass

if __name__ == '__main__':
    main()