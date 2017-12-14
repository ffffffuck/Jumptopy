N="abbccc"
N=list(N)
print(N)
n=""
for i in range(1,len(N)+1):
    if len(N) ==1:
        n = n +n[0]+'1'
        del N[0]
    if len(N) ==2:
        if N[0] != N[1]:
            n=n+N[0]+'1'
            del N[0]
        elif N[0] == N[1]:
            n=n+N[0]+'2'
            del N[0:2]
    if len(N) >2:
        if  N[i-1] != N[i]:
            n=n+N[0]+str(len(N[0:i]))
            del N[0:i]

print(N)
print(n)