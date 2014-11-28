__author__ = 'jefby'
#coding=utf-8

def vowels_count(string):
    '''
    :param string:
    :return:
    统计字符串string中元音字符的个数
    '''
    count = 0
    for c in string:
        if c in "aeiouAEIOU":
            count += 1
    return count

s = "abcdefg"
print vowels_count(s)


