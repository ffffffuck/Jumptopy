
m= 1
g=15*m
t= 60*m
a= 24*t
d=0
day = range(1,t*24+1)
# print(list(day))
for i in day:
    if i-t == g:
        d+=i
print(d)
z=[]
for i in day:
    if i%d ==0:
        z.append(i)

for i in z:
    t,m= divmod(i,60)
    # print(t,m)
