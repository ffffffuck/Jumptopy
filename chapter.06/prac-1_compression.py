N=str(input()+' ')
a=''
n=0
for i in range(len(N)-1) :
    if N[i] != N[i+1]:
        a= a+N[i]+str(n)
        n=1
    elif N[i] == N[i+1]:
        n+=1

print(a)

