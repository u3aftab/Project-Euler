# What is the smallest odd composite that cannot be written
# as the sum of a prime and twice a square?

import math

def is_prime(i):
    for x in xrange(2,int(i**0.5)+1):
        if i%x==0:
            return False
    return True

def i_can_be_written_as_composite(i):
    for x in p:
        i_Gb=((i-x)/2)**0.5
        if i_Gb-int(i_Gb)==0:
            return True
    return False

p=[2, 3, 5, 7]
i=9
bound=100000
while i<bound:
    if is_prime(i):
        p.append(i)
        i+=2
    else:
        if (not i_can_be_written_as_composite(i)) :
            print i
            break
        i+=2
        
        
