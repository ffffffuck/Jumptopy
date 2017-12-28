import random
n=0
g=0
for i in range(200000):
    a = random.random()
    b = random.random()
    if pow(a,2)+pow(b,2) <= 1:
        g+=1
        n+=1
    else:
        n+=1
print(g/n)
print(3.14/4)