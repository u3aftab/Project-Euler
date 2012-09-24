# Find the sum of all eleven primes that are both truncatable
# from left to right and right to left.

def is_prime(n):
    if n==0 or n==1: return False
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            return False
    return True

def trunc_left(n):
    if n<10:
        return is_prime(n)
    elif is_prime(n):
        return trunc_left(int(str(n)[1:]))
    else:
        return False

def trunc_right(n):
    if n<10:
        return is_prime(n)
    elif is_prime(n):
        return trunc_right(int(str(n)[:-1]))
    else:
        return False

def is_trunc(n): return trunc_left(n) and trunc_right(n)

trunc_primes=filter(is_trunc, xrange(10,1000000))

print trunc_primes
print "sum:", sum(trunc_primes)
