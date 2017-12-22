
def Josephus(N,K):
    N=list(range(1,N+1))
    cnt=1
    lst=[]
    while len(N) !=1:
        for i in N:
            if cnt%K ==0:
                lst.append(i)
            cnt+=1
        for j in lst:
            N.remove(j)
            lst=[]
            print(N)

Josephus(10,3)