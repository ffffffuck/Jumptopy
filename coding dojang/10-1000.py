print(sum(eval('*'.join(list(str(i)))) for i in range(10,int(input("입력하세요:"))+1)))

sum=0
for i in range(10,1000+1):
    x=1
    for j in str(i):
        x=x*int(j)
    sum=sum+x
print(sum)

