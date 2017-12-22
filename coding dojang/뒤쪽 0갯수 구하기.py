
N=int(input("입력"))
n=''
for i in range(1,N+1):
    n+=(str(i))+'*'

n=list(str((eval(n[:-1]))))
a=0
while int(n[-1]) < 1:
    n.pop()
    a+=1
print("%s 를 입력했을때 뒤에서 부터 연속되는 0의 갯수: %s개" %(N,a))

