input = '''
12.0 12.0 8.0
15.0 14.0 4.0
'''

def RT(x, y, z):
    n = (x ** 2 - (z / 2) ** 2) ** 0.5
    r = n / 4
    print('%0.3f' % round(r, 3))


input=input.split('\n')[1:-1]
for i in range(len(input)):
    x,y,z= map(float, input[i].split(' '))
    RT(x, y, z)






