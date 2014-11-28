__author__ = 'jefby'
#coding=utf-8
#根据列表元素的字符串长度进行排序，由长到短
words = ['hello','jefby','python']

words.sort(key = lambda x:len(x),reverse=True)
print words
