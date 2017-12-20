import re

n=3
n_list=[]
for i in range(0,10001):
    if i%2 ==1 and i%5 ==1:
        n_list.append(str(i))

for i in range(len(n_list)):
    if i%n == 0 :
        for a in (n_list):
            if p in a:
                print(a)
