input ='''
8
3 1 4 1 5 9 2 6
'''

a,b= input.split('\n')[1:-1]
a=int(a)
b=list(map(int,b.split(' ')))
n = 0
ss = 0
while True:
    s=0
    for i in range(len(b)-1):
        j=i+1
        if b[i]>b[j]:
            b[i],b[j]=b[j],b[i]
            s+=1
    n+=1
    if s is 0:
        break
    ss += s
print(n,' ',ss)

