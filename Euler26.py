def rep_len(n):
    dividend=pow(10,len(str(n)))%n
    l=[]
    while (dividend not in l) and not dividend==0:
        l.append(dividend)
        dividend=dividend*10%n
    return len(l)
        
max=0
d=2
while d<1000:
    if rep_len(d)>max:
        max=d
        d+=1
    else:
        d+=1
print max

        
    
