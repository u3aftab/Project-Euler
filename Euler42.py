f=open('Euler42_words.txt','r')
f=f.read().split(',')
tri_nums=map(lambda x: int(float(x)/2*(x+1)), xrange(501))
# assumed that there is no words whose sume exceeds 500 (~17 chars)

def word_sum(word):
    return sum(map(lambda x: ord(x)-64, word[1:-1]))

print len(filter(lambda x: word_sum(x) in tri_nums, f))
    
