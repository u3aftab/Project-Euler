## Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

upper=99999

def sum_of_5th_powers(n):
        return sum(int(x)**5 for x in str(n))

print sum(filter(lambda x: x==sum_of_5th_powers(x), xrange(10,1000000)))
