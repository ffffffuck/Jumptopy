
a,b = 'photography autograph'.split(' ')

def part(a):
    result=[]
    for i in range(len(a)):
        for j in range(len(a)):
            result.append(a[j:i+1])
    return result

result=[]
for i in part(b):
    if i in part(a):
        result.append(i)

g = 0
d = ''
for i in result:
    if len(i)>g:
        g=len(i)
        d=i

print(str(g)+'\n'+str(d))