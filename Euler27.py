def is_prime(n):
    n=abs(n)
    for i in xrange(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def seq_len(a, b):
    length=0
    i=0
    while True:
        if is_prime(i**2+a*i+b):
            length+=1
            i+=1
        else:
            return i 


largest_seq=((1,41), 41)
for a in xrange(-999,1000):
    for b in xrange(-999,1000):
        ab_seq_len=seq_len(a, b)
        if ab_seq_len>largest_seq[1]:
            largest_seq=((a, b), ab_seq_len)

print largest_seq[0][0]*largest_seq[0][1]
        
        
