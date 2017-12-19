def increae(n):
    str_n= str(n)
    rt = True
    for i in range(len(str_n)-1):
        rt = rt and str_n[i] <= str_n[i+1]
    return rt

count=0
for i in range(100,1000):
    if str(i)[-1] != 0 and increae(i*int(str(i)[::-1]))==1:
        count+=1

print(count)


