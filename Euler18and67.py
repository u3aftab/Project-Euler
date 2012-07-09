## 18/67)Find the maximum sum travelling from the top of the triangle to the base.

l=file('Euler18_triangle.txt')
m=file('Euler18_triangle.txt')

def format_triangle(f):
    num_list=f.readlines()
    for i in range(len(num_list)):
        num_list[i]=num_list[i].split(' ')
    for i in range(len(num_list)):
        for ii in range(len(num_list[i])):
            (num_list[i])[ii]=int((num_list[i])[ii])
    num_list.reverse()
    return num_list

def largest_sum(tri_list):
    i=1
    while i<len(tri_list):
        element=0
        while element<len(tri_list[i]):
            if (tri_list[i-1])[element]>(tri_list[i-1])[element+1]:
                (tri_list[i])[element]=(tri_list[i-1])[element]+(tri_list[i])[element]
            else:
                (tri_list[i])[element]=(tri_list[i-1])[element+1]+(tri_list[i])[element]
            element=element+1
        i=i+1
    return (tri_list[-1])[0]
    
print '18:', largest_sum(format_triangle(file('Euler18_triangle.txt')))
print '67:', largest_sum(format_triangle(file('Euler67_triangle.txt')))
