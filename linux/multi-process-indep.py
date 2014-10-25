__author__ = 'jefby'

from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s)...' %(name,os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.'% os.getpid()
    #create child process
    p=Process(target=run_proc,args=('test',))
    print 'Process will start'
    #start the child process
    p.start()
    #join function will wait for child process ends and continue to run
    p.join()
    print 'Process end.'


