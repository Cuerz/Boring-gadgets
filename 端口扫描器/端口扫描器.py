# -*- encoding: UTF-8 -*-
import socket
from optparse import OptionParser

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
    usage = "usage: xxx.py -i <ipaddress> -p <port>"    #帮助
    parser = OptionParser(usage=usage)          #添加usage方法，xx.py -h 就会出现以上的帮助
    parser.add_option("-i","--ip",type="string",dest="ipaddress",help="your target ip here")
    parser.add_option("-p","--port",type="string",dest="port",help="your target port here")
    (options,args) = parser.parse_args()        #获取选项和参数进行赋值

    ip = options.ipaddress
    port = options.port

    defaultport = [135, 139, 445, 1433, 3306, 3389, 5944]

    if ',' in port:             #xx.py -i [ip] -p 80,89,99
        port = port.split(',')
        a = []
        for x in port:
            a.append(int(x))
        scan(ip,a)

    elif '-' in port:           #xx.py -i [ip] -p 80-99
        port = port.split('-')
        s = int(port[0])
        e = int(port[1])
        rscan(ip,s,e)

    elif 'all' in port:         #xx.py -i [ip] -p all
        rscan(ip,1,65535)
    elif 'default' in port:     #xx.py -i [ip] -p default
        scan(ip,defaultport)


    pass


if __name__ == '__main__':
    main()