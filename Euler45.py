## After 40755, what is the next triangle
## number that is also pentagonal and hexagonal?

tri=(285, 40755)
pent=(165, 40755)
hexa=(143, 40755+1) ##incorrect hexagonal number

while tri[1]!=pent[1] or pent[1]!=hexa[1]:
    if tri[1]<pent[1]:
        n=tri[0]+1
        tri=(n, n*(n+1)/2)
    if pent[1]<hexa[1]:
        n=pent[0]+1
        pent=(n, n*(3*n-1)/2)
    if hexa[1]<tri[1]:
        n=hexa[0]+1
        hexa=(n, n*(2*n-1))

print tri[1]
