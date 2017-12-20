input='''
*...
....
.*..
....
'''

input=input.split('\n')[1:-1]
print(input)

A=[]
n=0
for i in range(len(input)):
    a=input[i]
    for i in range(len(a)):
        if a[i] == '.':
            A.append(0)
        elif a[i]=='*':
            A.append('*')

x=A[:4]
y=A[4:8]
g=A[8:12]
z=A[12:16]
print(z)
# print(x)
# print(y)
for i in range(0,len(x)):
    if x[i]=='*':
        if x[-2] != '*' and x[-1] != '*':
            x[-1] == 0
        else: x[i-1]=x[i-1]+1
        x[i+1]= x[i+1]+1
        y[i] = y[i]+1
        y[i-1] = y[i-1]+1
        y[i+1] = y[i+1]+1

    if y[i]=='*':
        if y[-2] != '*' and x[-1] != '*':
            y[-1] == 0
        else: y[i-1]=y[i-1]+1
        y[i+1]= y[i+1]+1
        x[i] = x[i]+1
        x[i-1] = x[i-1]+1
        x[i+1] = x[i+1]+1
        g[i] = g[i] + 1
        g[i - 1] = g[i - 1] + 1
        g[i + 1] = g[i + 1] + 1

    if g[i]=='*':
        if g[-2] != '*':
            g[-1] == 0
        else: g[i-1]=g[i-1]+1
        g[i+1]= g[i+1]+1
        y[i] = y[i]+1
        y[i-1] = y[i-1]+1
        y[i+1] = y[i+1]+1
        z[i] = z[i] + 1
        z[i - 1] = z[i - 1] + 1
        z[i + 1] = z[i + 1] + 1

    if z[i]=='*':
        if z[-2] != '*':
            z[-1] == 0
        else: z[i-1]=z[i-1]+1
        z[i+1]= z[i+1]+1
        g[i] = g[i]+1
        g[i-1] = g[i-1]+1
        g[i+1] = g[i+1]+1


print(','.join(map(str,x)))
print(','.join(map(str,y)))
print(','.join(map(str,g)))
print(','.join(map(str,z)))

