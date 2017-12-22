
input=int(input("숫자:"))
a,b=0,1
while b <= input:
    print(b)
    a,b = b,a+b



#정답
n=100
a=0;b=1
print('0', end='')
while b<=n:
    print(', %d'%b, end='')
    a,b = b,a+b
