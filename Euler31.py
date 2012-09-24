def vec_x(a, b):
    return sum(map(lambda x: x[0]*x[1], zip(a, b)))

import itertools

def how_many_ways(tup, use_each=True):         #each element must be used
    if sum(tup)==0 and use_each:
        return 0
    else




curr=[1, 2, 5, 10, 20, 50, 100, 200]

for i in xrange(1,9):
    cent_gen=itertools.combinations(curr, i)
    # using all the cents in the list that is indvidual cent_gen element,
    # how many ways can you sum to 200

