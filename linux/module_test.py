#!/usr/bin/env python
# -*- coding: utf-8 -*-

#first string will be as module document comment
' a test module '
#module author
__author__ = 'jefby'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello,world'
    elif len(args)==2:
        print 'Hello,%s!' % args[1]
    else:
        print 'Too many arguments!'
#when run in command mode ,python parse set __name__=__main__,
#and if not import this module,if judge will fail

if __name__ == '__main__':
    test()