## Find the sum of all pandigital numbers with an unusual
## sub-string divisibility property.

def sub_div(s_num, divisor, start, finish):
    if int(s_num[start:finish])%divisor==0:
        return True
    return False

ps=[2,3,5,7,11,13,17]
div_list=[(x,x+3) for x in xrange(1,8)]
div_list=zip(div_list, ps)
import itertools
sum=0
combs=itertools.permutations('0123456789', 10)
for i in combs:
    if i[0]=='0':
        continue
    i=reduce(lambda x, y: x+y, i)
    sign=True
    for j in div_list:
        if sub_div(i, j[1], j[0][0], j[0][1]):
            continue
        else:
            sign=False
            break
    if sign:
        sum+=int(i)
print sum
    

    
