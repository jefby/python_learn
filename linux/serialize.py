#!/usr/bin/env python
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob',age=2,score=98)

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
f.close
print d
