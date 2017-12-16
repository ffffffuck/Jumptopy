n= input('범위, 첫번째수,두번째수를 입력하세요.(종료:프로그램 종료):').split()
a=int(n[0])
b=int(n[1])
c=int(n[2])
d=[]
f=[]
g=[]
D=''
F=''
G=''
for i in range(b,a+1,b):
    d.append(i)
for i in range(c,a+1,c):
    f.append(i)
for i in range(b*c,a+1,b*c):
    g.append(i)
h=sum(set(d+f))
for i in d:
    D=D+str(i)+','
for i in f:
    F=F+str(i)+','
for i in set(d)|set(f):
    G=G+str(i)+','
w=set(d)|set(f)
D=D[:-1]
F=F[:-1]
G=G[:-1]
print("0부터 %s 이하의 범위를 선택하셨습니다. 이중에서\n%s의 배수는 %s 입니다.\n%s의 배수는 %s 입니다.\n%s과 %s의 배수는 %s 입니다.\n따라서 0부터 %s이하의 범위내에서 %s와 %s의 배수의 총합은 %s 입니다" %(a,b,D,c,F,b,c,G,a,b,c,h))