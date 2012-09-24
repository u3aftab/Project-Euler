def how_many_rights(p):
    i=0
    for a in xrange(1,p/3):
        for b in xrange(p/3,p/2):
            if  a+b+(a**2+b**2)**0.5==p:
                i+=1
    return i

max_rights=(0, 0)   #(p, number of rights)
for i in xrange(3,1001):
    i_rights=how_many_rights(i)
    if i_rights>max_rights[1]:
        max_rights=(i, i_rights)
print max_rights[0]
