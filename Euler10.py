## 10)Calculate the sum of all the primes below two million.

bound=2000000
plist=range(2,bound)
prime_sum=0
while plist[0]<bound**0.5+1:
    prime_sum=prime_sum+plist[0]
    plist=filter(lambda x: x%plist[0]!=0, plist)

prime_sum=prime_sum+sum(plist)
print prime_sum


    
            
