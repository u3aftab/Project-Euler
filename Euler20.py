## 20)Find the sum of digits in 100!

import math
print sum(map(lambda n: int(n),list(str(math.factorial(100)))))
