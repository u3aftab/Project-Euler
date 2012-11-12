## What is the largest 1 to 9 pandigital that can be formed
#3 by multiplying a fixed number by 1, 2, 3, ... ?

i=1
largest=0
while i<9999:
    prod=str(i)
    a=2
    while len(prod)<8:
        prod+=str(i*a)
        a+=1
    if len(prod)==9 and len(set(prod))==9 and int(prod)>largest and '0' not in set(prod):
        largest=int(prod)
    i+=1

print largest


