## 16)What is the sum of the digits of the number 2**1000?

l=str(2**1000)
l=list(l)
print sum(map(int, l))
