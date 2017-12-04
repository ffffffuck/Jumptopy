a = [-1,1,3,-2,2]
pp=[]
dd=[]
for i in range(len(a)):
    if a[i]<0:
        pp.append(a[i])
    else:
        dd.append(a[i])
print(len(a))
print(pp + dd)

