N=list(map(str, range(1,20+1)))
input='''
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
'''

input=input.split('\n')[1:-1]
for i in range(len(input)):
    a,b = map(int,input[i].split(' '))
    if a == 1:
        N[a - 1:b] = N[b - 1::-1]
    else:
        N[a-1:b]=N[b-1:a-2:-1]
print(N)

