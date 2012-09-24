special_fracs=[]
for num in xrange(10,100):
    for den in xrange(10,100):
        if den%10==0 or (num%11 and den%11)==0:
            continue
        if float(num)/den==float(str(num)[0])/int(str(den)[1]) \
           and str(num)[1]==str(den)[0] and float(num)/den<1:
            special_fracs.append((num,den))
       
def gcd(a,b):
    if a==0: return b
    elif b==0: return a
    else: return gcd(b, a%b)

num_of_prod=reduce(lambda x, y: x*y, [a[0] for a in special_fracs])
den_of_prod=reduce(lambda x, y: x*y, [a[1] for a in special_fracs])

print den_of_prod/gcd(num_of_prod, den_of_prod)
