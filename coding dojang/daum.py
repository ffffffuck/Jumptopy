import random

s= sorted(list(set(list(random.randint(1,100)for i in range(10)))))
print(s)
# s=[1, 2, 7, 8, 13, 15, 17, 20]

a=[s[i+1]-s[i] for i in range(len(s)-1)]
for i in range(len(s)-1):
    if s[i+1]-s[i] ==min(a):
        print(s[i] , s[i+1])



