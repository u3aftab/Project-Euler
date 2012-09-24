# Find the sum of all numbers that can be written as pandigital products.

s=str
digs=[s(i) for i in xrange(1,10)]
l=[a+b+c+d+e for a in digs for b in digs
   for c in digs for d in digs for e in digs]

def is_unusual_num(ns, i):
    if len(set(ns))<4:
        return False
    product=int(ns[:i])*int(ns[i:])
    if '0' in str(product):
        return False
    if (len(set(set(ns) | set(str(product))))==9) and product<10000:
        return product           
    return False

i_1=map(lambda x: is_unusual_num(x, 1), l)
i_2=map(lambda x: is_unusual_num(x, 2), l)
i_3=map(lambda x: is_unusual_num(x, 3), l)
i_4=map(lambda x: is_unusual_num(x, 4), l)

print sum(set(i_1+i_2+i_3+i_4))
            


