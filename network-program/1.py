__author__ = 'jefby'
#coding=utf-8

'''
This program is optimized for Python 2.7.It may run on any other Python version
with/without modifications

'''

import socket

def print_machine_info():
    #获取主机名
    host_name = socket.gethostname()
    print "Host name : %s" % host_name
    #获取当前IP地址
    ip_addr = socket.gethostbyname(host_name)
    print "IP address: %s" % ip_addr


if __name__ == '__main__':
    print_machine_info()