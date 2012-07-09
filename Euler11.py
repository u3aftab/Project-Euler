## 11)What is the greatest product of four adjacent numbers on the same
## straight line in the 20 by 20 grid?

grid=file('Euler11_Grid.txt', 'r')
num_list=grid.readlines()
for i in range(20):
    num_list[i]=num_list[i].split(' ')
num_list=sum(num_list,[])
for i in range(20*20):
    num_list[i]=int(num_list[i])

def list_prod(l):
    total=1
    for i in l:
        total=total*i
    return total

product=0
i=0

while i<=396:
    if list_prod((num_list[i:i+4]))>product:
        product=list_prod((num_list[i:i+4]))
        i=i+1
           
    else:
        i=i+1

while i<=339:
    if list_prod([num_list[i],num_list[i+20],num_list[i+40],num_list[i+60]])>product:
        product=list_prod([num_list[i],num_list[i+20],num_list[i+40],num_list[i+60]])
    else:
        i=i+1

for line in range(17):
    for step in range(16):
        if list_prod([num_list[line*20+step],num_list[(line+1)*20+1+step],num_list[(line+2)*20+2+step],num_list[(line+3)*20+3+step]])>product:
            product=list_prod([num_list[line*20+step],num_list[(line+1)*20+1+step],num_list[(line+2)*20+2+step],num_list[(line+3)*20+3+step]])

for line in range(17):
    for step in range(3,20):
        if list_prod([num_list[line*20+step],num_list[(line+1)*20-1+step],num_list[(line+2)*20-2+step],num_list[(line+3)*20-3+step]])>product:
            product=list_prod([num_list[line*20+step],num_list[(line+1)*20-1+step],num_list[(line+2)*20-2+step],num_list[(line+3)*20-3+step]])
        
print product        
        
        


           
                       
            



