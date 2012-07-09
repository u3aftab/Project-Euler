##22)What is the total of all the name scores in the file of first names?

a=file('Euler22_names.txt')
names=a.readlines()
names=names[0].split(",")
names.sort()

def name_to_alpha_sum(str):
    i=0
    for char in str[1:-1]:
        i=i+ord(char)-64
    return i

print sum(map(lambda name: name_to_alpha_sum(name)*(names.index(name)+1), names))

        

    
