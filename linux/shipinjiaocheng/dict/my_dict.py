__author__ = 'jefby'
#coding=utf-8
#统计字符串中的字母个数
count = {}
for i in 'aabbccd':
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print count
'''
#读取小说"emma.txt"，求其出现次数最多的前10个单词
f = open('emma.txt')
count = {}
for line in f:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
word_freq = []
for word,freq in count.items():
    word_freq.append((freq,word))
word_freq.sort(reverse=True)
for freq,word in word_freq[:10]:
    print word,freq
'''
#翻转字典
d = {'jefby':30,'hello':20,'python':20}

def reverse_dict(d):
    reverse = {}
    for k,v in d.items():
        if v in reverse:
            reverse[v].append(k)
        else:
            reverse[v] = [k]
    return reverse

r = reverse_dict(d)
print r