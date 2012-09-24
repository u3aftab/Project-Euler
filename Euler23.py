# Find the sum of all the positive integers which cannot be written
# as the sum of two abundant numbers.

bound=28123+1

def divisors(n):    #proper divisors
    return [i for i in xrange(1,n/2+1) if n%i==0]

ab_nums=filter(lambda n: sum(divisors(n))>n, xrange(1,bound))
ab_nums=[i+j for i in ab_nums for j in ab_nums if i+j<=bound]
ab_nums=set(ab_nums)
print sum(filter(lambda x: x not in ab_nums, xrange(1,bound)))
