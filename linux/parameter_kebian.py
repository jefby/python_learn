#!/usr/bin/env python
# coding=utf-8

def calc(*numbers):
	sum = 0
	for i in numbers:
		sum = sum + i * i
	return sum

#numbers = raw_input('please input the numbers:')
numbers = [1,2,3,4]
print calc(*numbers)
