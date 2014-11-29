#!/usr/bin/env python
#coding=utf-8

import ntplib 
from time import ctime

def print_time(ntp_server):
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request(ntp_server)
    print ctime(response.tx_time)


if __name__ == '__main__':
    print_time('time.pool.aliyun.com')
