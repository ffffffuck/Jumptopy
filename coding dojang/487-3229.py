input = '''
12
4873279
ITS-EASY
888-4567
3-10-10-10
888-GLOP
TUT-GLOP
967-11-11
310-GINO
F101010
888-1200
-4-8-7-3-2-7-9-
487-3279
'''
dic={
    'ABC':'2',
    'DEF':'3',
    'GHI':'4',
    'JKL':'5',
    'MNO':'6',
    'PRS':'7',
    'TUV':'8',
    'WXY':'9',
}

def find_key(n):
	dic_a = list(dic)
	for i in dic_a:
		if n in i:
			return dic[i]

output=[]
n=0
input= input.split("\n")[1:-1]	
for i in range(1, len(input)):
	a=input[i]
	for i in range(len(a)):
		if a[i] == '-': continue
		if a[i].isalpha(): 
			output.append(find_key(a[i]))
		else: output.append(a[i])
		n=n+1
		if n %7==0 : output.append('\n')				
output=''.join(output)
output= output.split('\n')[:-1]
output=list(map(int, output))
output.sort()
output.reverse()
count=0
for i in range(len(output)-1):
	if output.count(output[i]) > 1:
		print(str(output[i])[:3], '-', str(output[i])[3:],output.count(output[i]))
	else: print("no duplicated")


print(output)
print(input)		

