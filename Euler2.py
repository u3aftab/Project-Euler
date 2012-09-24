## 2) By considering the terms in the Fibonacci sequence whose
## values do not exceed four million, find the sum of the even-valued terms.

def even_fib(upper):
	x1=1
	x2=2
	temp=x2
	sum=0
	while x2<upper:
		if x2%2==0:
			sum=sum+x2
		x2=x1+x2
		x1=temp
		temp=x2
	print sum

even_fib(4000000)

# Refractored code

x_1, x= 1, 1
even_sum=0
while x<4000000:
    if x%2==0:
        even_sum+=x
    x_1, x= x, x_1+x
print even_sum
