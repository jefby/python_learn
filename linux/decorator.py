#!/usr/bin/env python
def log(func):
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return wrapper
@log
def now():
    print '2014-10-22'
now()
