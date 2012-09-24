def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

primes=filter(is_prime, xrange(1000,10000))

p_len=len(primes)
for i in xrange(p_len):
    for j in xrange (i+1, p_len):
        if set(str(primes[i]))==set(str(primes[j])):
            p_i=primes[i]
            p_j=primes[j]
            for k in xrange(j+1, p_len):
                p_k=primes[k]
                if set(str(p_i))==set(str(p_k)):
                    if p_j-p_i==p_k-p_j:
                        print str(p_i)+str(p_k)+str(p_k)
            
                   


