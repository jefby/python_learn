__author__ = 'jefby'
#coding=utf-8

#求解一元二次方程
import math
a,b,c=eval(raw_input("please input 3 intergers:"))
if a != 0:
    delta = b*b-4*a*c
    if delta < 0:
        print "without result"
    elif delta == 0:
        print "only one result,res=%-.2f"%((math.sqrt(delta)-b)/2.0/a)
    else:
        res1 = (math.sqrt(delta)-b)/2.0/a
        res2 = (-math.sqrt(delta)-b)/2.0/a
        print "res1=%-.2f"%res1+",res2=%-.2f"%res2
else:
    print "this is linear equation."






