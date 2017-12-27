import random

n=0
g=0
for i in range(100000):
    a = random.random()
    b = random.random()
    if pow(a,2)+pow(b,2) <= 1:
        n+=1
    else:
        n+=1
        g+=1


print(a)
print(b)
print(n)
print(g)

print(g/n)
print(3.14/4)