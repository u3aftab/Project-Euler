## Find the last ten digits of 1**1 + 2**2 + ... + 1000**1000.

a=0
for i in xrange(1,1001):
    a+=i**i
print str(a)[-10:]
