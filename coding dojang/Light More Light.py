input='''
3
6241
8191
'''
input=input.split('\n')[1:-1]

def light(input):
    for i in range(len(input)):
        n=int(input[i])
        switch = 'OFF'
        for i in range(1,n+1):
            if n%i ==0 and switch =='OFF':
                switch ='ON'
            elif n%i ==0 and switch == 'ON':
                switch = 'OFF'
        if switch =='OFF':print("NO")
        else : print("YES")

light(input)