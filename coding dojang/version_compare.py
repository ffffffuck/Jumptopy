# N = '0.0.3.4,0.034.5'.split(',')
N=input("버전 입력").split(',')
a= N[0].split('.')
b= N[1].split('.')
A=''
B=''
for i in a:
    A=A+i
for i in b:
    B=B+i
if A > B :
    print(N[0],'>',N[1])
elif A < B :
    print(N[0], '<', N[1])
else :
    print(N[0],'=', N[1])