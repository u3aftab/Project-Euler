# Find the smallest pair of pentagonal numbers
# whose sum and difference is pentagonal.

def p(n):
    return n*(3*n-1)/2

i=3
penta=[1, 5]
sums=set()
p_i=p(i)
while p_i not in sums:
    for x in xrange(len(penta)):
        if p_i-penta[x] in penta[:x]:
            sums.add(p_i+x)
    penta.append(p_i)
    i+=1
    p_i=p(i)
    
        

