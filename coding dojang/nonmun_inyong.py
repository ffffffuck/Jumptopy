input = input('넣어')
# 리스트에서 0빼기
a=[]
for i in [int(i) for i in input.split()]:
    if int(i) > 0 :
        a.append(i)
print(a)

# h-index
b=[]
for i in range(len(a)):
    if a[i] > len(a): pass
    elif a[i] <= len(a):
        b.append(a[i])
try:
    b=max(b)
    print("h-index:",b)
except:print("h-index:0")

# g-index
sum=0
for i in a :
    sum=sum+i
print("g-index:",int(sum**0.5))