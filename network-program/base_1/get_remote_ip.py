__author__ = 'jefby'
#coding=utf-8
#get remote ip address

import socket
#定义函数
def get_remote_machine_info(remote_host):
    #remote_host = 'www.baidu.com'
    try:
        print "IP Address of %s : %s" %(remote_host,socket.gethostbyname(remote_host))
    except socket.error,err_msg:
        print "%s:%s" %(remote_host,err_msg)

if __name__ == '__main__':
    #输入远程域名
    remote_host = raw_input("please input the remote host:")
    get_remote_machine_info(remote_host)


