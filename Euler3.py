## 3)Find the largest prime factor of a composite number.

def is_prime(n):
    check_div=2
    while check_div<n/2+1:
        if n%check_div==0:
            return False
        check_div=check_div+1
    return True

def largest_prime_factor(n):
    plist=[1]   #list of prime factors of n
    if n%2==0:
        plist.append(2)
        n=n/2
    if n%3==0:
        plist.append(3)
        n=n/3
    count=5
    while count<=n:
        if n%count==0 and is_prime(count):
            plist.append(count)
            n=n/count
            count=count+2
        if n%count==0:
            n=n/count
            count=count+2
        else:
            count=count+2
    return plist[-1]
        
print largest_prime_factor(600851475143)        
