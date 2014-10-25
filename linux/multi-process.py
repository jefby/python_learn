'multiple process example'
#multi-process.py
__author__ = 'jefby'

import os
print 'Process (%s) starting...' %os.getpid()
#create new process
pid=os.fork()
#child process
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid())
else:
    print 'I (%s) just create a child process(%s)' %(os.getpid(),pid)



