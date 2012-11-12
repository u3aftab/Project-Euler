# Find the first four consecutive integers to have four distinct
# primes factors.  What is the first of these numbers?

def prime_factor(n, i=2, j=0):
    if j==0: j=int(n**0.5)+2
    for p in xrange(i, j):
        if n%p==0:
            return [p]+prime_factor(n/p, p, j)
    if j!=0 and n!=1: return [n]
    return []

consec=4

in_a_row=0
nums=[]
i=2
while in_a_row!=consec:
    if len(set(prime_factor(i)))==consec:
        nums.append(i)
        in_a_row+=1
        i+=1
    elif nums==[]:
        i+=1
        continue
    else:
        nums=[]
        in_a_row=0

print nums
        

        
        
