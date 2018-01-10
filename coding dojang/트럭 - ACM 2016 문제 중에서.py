input='''
10 100 100
10 10 10 10 10 10 10 10 10 10
'''

a,b=input.split('\n')[1:-1]

n,w,L=a.split(' ')

b=list(map(int,b.split(' ')))

print(b)


g= int(L)/int(n)

n=0
for i in range(len(b)):
    if b[i]>g:
        n+=2
    elif b[i]<g:
        n+=1

print(n)