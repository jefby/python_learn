__author__ = 'jefby'

from multiprocessing import Process,Queue
import os,time,random

#write date process
def write(q):
    for value in ['A','B','C']:
        print 'Put %s to queue...'%value
        q.put(value)
        time.sleep(random.random())

#read data process
def read(q):
    while(True):
        value = q.get(True)
        print 'Get %s from queue.'%value

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    #wait pw ends
    pw.join()
    pr.terminate()


