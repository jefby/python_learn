__author__ = 'jefby'
#coding=utf-8
'''
读取文件中的人名并将其格式化为首字母大写其他字符小写格式
'''
def is_palindrome(string):
    low = 0
    up = len(string)-1
    while low < up:
        print 'low is ',string[low]
        print 'up is',string[up]
        if string[low] != string[up]:
            return False
        else:
            low += 1
            up -= 1
    return True


def is_ascending(string):
    p = string[0]
    for c in string:
        if p > c:
            return False
        else:
            p = c
    return True

import re

f = open('names.txt')

pattern = 'C.A'

for line in f:
    name = line.strip()
    result = re.search(pattern,name)
    if result:
        print name.title()

f.close()

sep = '+'
#将序列转换为str方法：''.join(seq)
sep = ''
seq = ['1','2','3','4','5']
print sep.join(seq)


dirs = '','usr','bin','env'
print type(dirs)
new_dirstr = '/'.join(dirs)
print new_dirstr.split('/')#split是join的逆函数，用于分割字符串
print '          internal whitespace   is keep for strip  '.strip()

def hello(name):
    print 'hello',name

map(hello,['jefby','yrh','haha'])

