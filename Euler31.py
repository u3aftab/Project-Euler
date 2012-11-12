## How many different ways can $2 be made using any number of coins?
## 1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).

def not_in(l1, l2): ##l2 is a list of lists
    for x in l1:
        l2=filter(lambda y: x not in y, l2)
    return l2

coins=[1, 2, 5, 10, 20, 50, 100, 200];
combs=[[], [[1]], [[2], [1, 1]]]
i=3
coins_curr_index=2 #include this many first values from coins 
while i<201:
    temp=[]
    for x in xrange(coins_curr_index):
        valid_arrs=not_in(coins[:x] ,combs[i-coins[x]])
        for each_arr in valid_arrs:
            temp.append(each_arr+[coins[x]])                      
    if i==coins[coins_curr_index]:
        coins_curr_index+=1
        temp.append([i])
    combs.append(temp)
    i+=1
print len(combs[200])
