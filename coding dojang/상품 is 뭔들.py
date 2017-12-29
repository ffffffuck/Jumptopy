def yak(x):
    d=0
    for i in range(1,x+1):
        if x%i ==0:
            d+=1
    return d

a,b = map(int,input("정수 입력:").split(' '))
n=0
g=0
for i in range(a+1,b+1):
    if  yak(i)%2==1:
        n=n+1
        g=g+1
    else: n+=1

if n%g == 0:
    print('1'+'/'+str(int(n/g)))
else:
    print(str(g)+'/'+str(n))

