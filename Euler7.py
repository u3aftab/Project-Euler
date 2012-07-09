## 7)Find the 10001st prime.

def is_prime(n):
    check_div=2
    while check_div<n/2+1:
        if n%check_div==0:
            return False
        check_div=check_div+1
    return True

def nth_prime(n): # finds the nth prime number where n is a prime > 2
    counter=2
    curr_num=3
    while counter<=n:
        if is_prime(curr_num):
            counter=counter+1
        curr_num=curr_num+2
    print curr_num-2

nth_prime(10001)
