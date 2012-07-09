## 9)Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000.

import math
for x in range(1000):
        for y in range(1000):
            a=x
            b=y
            c=math.sqrt(a**2+b**2)
            if a+b+c==1000:
                print [a,b,c], a*b*c
    


    
    
    
    
