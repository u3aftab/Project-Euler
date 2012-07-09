## 17)How many letters would be needed to write all the numbers in words from 1 to 1000?

units=['one','two','three','four','five','six','seven','eight','nine']
ten='ten'
teens=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tys=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def num_to_words(n): # n<9999
    if n<=9:
        return units[n-1]
    if n==10:
        return ten
    if n>=11 and n<=19:
        return teens[n%10-1]
    if n>=20 and n<=99:
        if n%10==0:
            return tys[n/10-2]
        else:
            return num_to_words(n-(n%10))+'-'+num_to_words(n%10)
    if n>=100 and n<=999:
        if n%100==0:
            return num_to_words(n/100)+' '+'hundred'
        else:
            return num_to_words(n-n%100)+' and '+num_to_words(n%100)
    if n>=1000 and n<=9999:
        if n%1000==0:
            return num_to_words(n/1000)+' '+'thousand'
        else:
            return num_to_words(n-n%1000)+' '+num_to_words(n%1000)

upper=1000 #the letter-lenght of numbers in words, up to and including upper is summed
print sum(map(lambda x: len(x),
              map(lambda y: y.replace(' ','').replace('-',''),
                  map(num_to_words, range(1,upper+1)))))
              
            
