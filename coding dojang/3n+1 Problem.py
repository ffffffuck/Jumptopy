def cycle(n):
    number = 1
    while n !=1:
        if n%2==0:
            n=n//2
            number+=1
        elif n%2==1:
            n=n*3+1
            number+=1
    return number
input='''
1 10
100 200
201 210
900 1000
'''
result=[]
input=input.split('\n')[1:-1]
for i in input:
   a=i.split(' ')[0]
   b=i.split(' ')[-1]
   g=0
   for n in range(int(a),int(b)+1):
       if cycle(n) > g:
           g = cycle(n)
   result.append(str(g))

for i in range(len(input)):
    print("%s %s"%(input[i], result[i]))
