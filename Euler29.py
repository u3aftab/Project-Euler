﻿# How many distinct terms are in the sequence generated by
# ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

print len(set((a**b for a in xrange(2,101) for b in xrange(2,101))))
