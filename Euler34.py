import math
mf=math.factorial

def cur_num(n):
    return n==sum((mf(int(i)) for i in str(n)))

filter(cur_num, xrange(3, 1000000))
