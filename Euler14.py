## 14)Find the longest sequence using a starting number under one million.

nat_num=3
l=[1,2]
count=0
i=3
while nat_num<1000000:
    if i<=len(l):
        l.append(count+l[i-1])
        nat_num=nat_num+1
        count=0
        i=nat_num
    elif i%2==0:
        i=i/2
        count=count+1
    else:
        i=3*i+1
        count=count+1

print l.index(max(l))+1
