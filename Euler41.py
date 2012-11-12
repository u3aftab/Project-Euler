def is_prime(n):
    for i in xrange(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

import itertools

dig_str='123456789'
i_str_lst=[]
for i in xrange(9,1,-1):
    dig_str_instance=dig_str[:i]
    for i in itertools.permutations(dig_str_instance, i):
        num_i=int(''.join(i))
        if is_prime(num_i):
            i_str_lst.append(num_i)
    if len(i_str_lst)>1:
        break

print max(i_str_lst)
