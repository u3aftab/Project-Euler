## 12)What is the value of the first triangle number
## to have over five hundred divisors?

def pow_of_n(k,n):
    i=0
    while k%n==0:
        i=i+1
        k=k/n
    return i
        
def num_of_divisors(n):
    pow_of_2=pow_of_n(n,2)
    pow_of_3=pow_of_n(n,3)
    n=n/(2**pow_of_2 * 3**pow_of_3)
    num=(pow_of_2+1)*(pow_of_3+1)
    curr_prime=5
    while n!=1:
        curr_prime_power=pow_of_n(n,curr_prime)
        num=num*(1+curr_prime_power)
        n=n/(curr_prime**curr_prime_power)
        curr_prime=curr_prime+2
    return num

divisors=0
k=8
while divisors<500:    
    divisors=num_of_divisors(k*(k+1)/2)
    k=k+1
print 'num:',(k-1)*k/2
print 'num of divisors:', divisors
print 'nth triangle number:', k-1












        
