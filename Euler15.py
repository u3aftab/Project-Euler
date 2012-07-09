## 15)Starting in the top left corner in a 20 by 20 grid,
## how many routes are there to the bottom right corner?

l=[[2]]
i=3
while i<=40:
    ith_row=[i]
    k=0 
    while k<i:
        if k==i-3:
            ith_row.append(i)
            k=k+3
        else:
            ith_row.append(i_minus_1_row[k]+i_minus_1_row[k+1])
            k=k+1
    l.append(ith_row)
    i_minus_1_row=ith_row
    i=i+1

fourtyth_row=l[-1]
print fourtyth_row[19]
