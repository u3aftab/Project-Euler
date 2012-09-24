# Which prime, below one-million,
# can be written as the sum of the most consecutive primes?

def is_prime(n):
    for i in xrange(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

upper=1000000
p=[2]+filter(is_prime, xrange(3, upper, 2))
psums=[2]
for i in xrange(1,len(p)):
    psums.append(psums[i-1]+p[i])
psums_set=set(psums)
max_so_far=(2, 0)  #prime, number of consec in sum

for i in xrange(len(p)-1, 0, -1):
    if p[i] in psums_set:
        max_so_far=(p[i], psums.index(p[i]))
        break
        
del psums_set
p=p[p.index(max_so_far[0]):]
   
q=0
for i in xrange(len(p)):
    s=1
    q=i
    e=1+max_so_far[1]
    while psums[e]-psums[s]!=p[i]:
        if psums[e]-psums[s]>p[i]:
            s+=1
        if psums[e]-psums[s]<p[i]:
            e+=1
        if e-s<max_so_far[1]:
            continue
        if psums[e]-psums[s]==p[i]:
            max_so_far=(p[i], e-s)

print max_so_far
    
           

    
