__author__ = 'jefby'

# compute e's value
# e= 1+ 1/1!+1/2!+1/3!+....

en_1 = 1
n = 1
factorial = 1
invfactorial = 1

while invfactorial > 1e-6:
    en = en_1 + invfactorial
    n = n + 1
    factorial *= n
    invfactorial = 1.0 / factorial
    en_1 = en
print "e = %-.5f"%en

