__author__ = 'jefby'
#coding=utf-8
#交换lst中的元素lst[a]和lst[b]的值
def swap(lst,a,b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp
#lst左移一位
def shift_left(lst):
    tmp = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i+1]
    lst[-1] = tmp

#线性查找方法：查找lst中是否有值为v的元素，如果有，返回其下标；否则返回-1
def search(lst,v):
    for i in range(len(lst)):
        if lst[i] == v:
            return i
    return -1

#二分查找
def bi_search(lst,v):
    low = 0
    high = len(lst)
    while low <= high:
        mid = (low+high)/2
        if v == lst[mid]:
            return mid
        elif v > lst[mid]:
            high += 1
        else:
            low -= 1
    return -1

x = [10,20,30]
shift_left(x)
print x

#print x.index(40)
y = [1,2,3,4,100,7,8]
y.sort()#排序


print y
print bi_search(y,100)

x = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print len(x[0])
#返回第二个元素
def f(lst):
    return lst[1]



students = [['zhang',89],['wang',92],['Li',100],['zhao',77]]
#students.sort(key = f,reverse=1)#逆序排序
students.sort(key = lambda x:x[1],reverse=1)#逆序排序
print students
print float(sum(student[1] for student in students)) / len(students)