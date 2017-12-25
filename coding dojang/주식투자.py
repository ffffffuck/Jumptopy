a = 10000
g = a
b = 4
c = [10,-10,5,-5]

for i in range(b):
    a = a+a*(c[i]/100)

print(round(a-g))
if a/g >1:
    print('good')
elif a/g < 1:
    print('bad')
elif -0.5 < a/g < 0.5:
    print('same')

