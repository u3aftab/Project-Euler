# Rinite summation formulas
# 1+2+...+n=n*(n+1)/2
def lin_sum(n):
    return n*(n+1)/2
# 1**2+2**2+...+n**2=n*(n+1)*(2n+1)/6
def lin_sum_sq(n):
    return n*(n+1)*(2*n+1)/6



## 1)Find the sum of all the multiples of 3 or 5 below 1000.
print '1:',3*lin_sum(333)+5*lin_sum(199)-15*lin_sum(66)

## 5)What is the smallest number divisible by each of the numbers 1 to 20?
print '5:',2*3*2*5*7*2*3*11*13*2*17*19

## 6)What is the difference between the sum of the squares and the square
## of the sums?
print '6:',lin_sum(100)**2 - lin_sum_sq(100)

##25) What is the first term in the Fibonacci sequence to contain 1000 digits?
#solve floor((phi**n)/(5**.5)+.5)<=1e**999 for n. n=4782
print '25:4728'
