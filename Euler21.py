## 21)Evaluate the sum of all amicable pairs under 10000.

def sum_of_div(n):
    i=1
    sum=0
    while i<=n/2:
        if n%i==0:
            sum=sum+i
        i=i+1
    return sum

def amicable_number(n):
    sum_n=sum_of_div(n)
    sum_sum_n=sum_of_div(sum_n)
    if n!=sum_n and n==sum_sum_n:
        return True
        print n
    else:
        return False

upper=10000 # upper bound on the range of numbers that will be check for amicability

print sum(filter(amicable_number, range(2,upper)))
