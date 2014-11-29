__author__ = 'jefby'
#coding=utf-8

import socket
import struct
import sys
import time

#NTP SERVER IP Address
NTP_SERVER = "time.pool.aliyun.com"
#1970年1月1日0时0分0秒值
TIME1970 = 2208988800L

def sntp_client():
    #创建UDP套接字
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    data = '\x1b'+47 * '\0'
    #发送协议数据
    client.sendto(data,(NTP_SERVER,123))
    #从NTP服务器接收到的响应
    data,address = client.recvfrom(1024)
    if data:
        print 'Response received from:',address
    t = struct.unpack('!12I',data)[10]
    #求从格林尼治时间后经过的秒数
    t -= TIME1970
    #转换为用户可读时间格式
    print'\tTime=%s'%time.ctime(t)

if __name__ == '__main__':
    sntp_client()
