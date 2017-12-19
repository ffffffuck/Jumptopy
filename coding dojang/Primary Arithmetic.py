input = '''
123 456
569 239
999 99
'''
# input=input.split('\n')
N=[i.split(' ') for i in input[1:-1].split('\n')]

for i in N:
    a=i[0][::-1]
    b=i[1][::-1]
    print(a,b)
    n = 0
    puton=0
    if len(str(a)) == len(str(b)):
        for i in range(len(str(int(a)))):
            if int(str(a)[i])+ int(str(b)[i]) +puton >= 10:
                n=n+1
                # puton=1
    if len(str(a)) > len(str(b)):
        for i in range(len(str(int(b)))):
            if int(str(a)[i])+ int(str(b)[i]) +puton >= 10:
                n = n + 1
                puton = 1
    if len(str(a)) < len(str(b)):
        for i in range(len(str(int(a)))):
            if int(str(a)[i]) + int(str(b)[i]) + puton >= 10:
                n=n+1
                puton=1
    if n == 0:
        print('No carry operation.')
    else:
        print('%s carry operation.' %n)


print(ord('똘'))
# len(str(int(a)+1))

