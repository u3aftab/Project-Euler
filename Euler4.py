## 4)Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(str): # takes a strings and returns a boolean indicating
                        # whether the inputed string is a palindrome
    if len(str)<=1:
        return True
    elif str[0]==str[-1]:
        return is_palindrome(str[1:-1])
    else:
        return False

largest=9009
for a in range(100,1000):
    for b in range (999,99,-1):
        if is_palindrome(str(a*b)) and a*b>largest:
            largest=a*b
print largest
            
        
