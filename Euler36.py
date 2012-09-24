def pal_in_both(n):
    if str(n)==str(n)[::-1]:
        if bin(n)[2:]==bin(n)[2:][::-1]:
            return True
    return False

print sum(filter(pal_in_both, xrange(1000000)))
