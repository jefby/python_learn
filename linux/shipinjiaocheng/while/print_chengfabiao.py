__author__ = 'jefby'

for i in range(1,10):
    for j in range(1,1+i):
        print str(i)+'*'+str(j)+'='+str(i*j),
    print


for i in range(1,3):
    for j in range(1,3):
        if i*j < 2:
            continue
        print i*j

