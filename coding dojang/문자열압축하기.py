n= input("입력하쇼잉:")
a=1
result=''
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        result+=n[i]+str(a)
        a=1
    else: a+=1
result+=n[-1]+str(a)
print(result)

