## 13)Find the first ten digits of the sum of one-hundred 50-digit numbers.

l=file('Euler13_list.txt')
num_list=l.readlines()
for i in range(100):
    num_list[i]=int(num_list[i])
digits=str(sum(num_list))
print digits[0:10]
