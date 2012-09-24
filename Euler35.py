# How many circular primes are there below one million?

def primes_below(n):
    p_list=range(2,n)
    i=0
    while i<=int(len(p_list)**0.5)+1:
        p_list=p_list[:i+1]+filter(lambda x: x%p_list[i]!=0, p_list[i+1:])
        i+=1
    return p_list

def rotate(n):
    str_n=str(n)
    return int(str_n[1:]+str_n[0])

p_list=primes_below(1000000)
no_evens=[]
for x in p_list:
    str_x=str(x)
    if ('2' in str_x) or ('4' in str_x) or ('6' in str_x) or ('8' in str_x) or ('0' in str_x):
        continue
    else:
        no_evens.append(x)

no_evens=set(no_evens)
for x in xrange(5):
    temp=map(rotate, no_evens)
    temp=set(temp)
    no_evens=temp & no_evens

print len(no_evens)+1  # +1 for 2 that is removed earlir
