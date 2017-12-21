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

count_dic={}
input= input.split("\n")[2:-1]
for i in range(len(input)):
	input[i]= input[i].replace("-","")
	input[i]=input[i][:3]+'-'+input[i][3:]
	for j in range(len(input[i])):
		if input[i][j].isalpha():
			input[i] = input[i].replace(input[i][j], find_key(input[i][j]))
	count_dic[input[i]] = input.count(input[i])
input=sorted(list(set(input)))
for i in input:
	if count_dic[i] > 1:
		print(i, count_dic[i])
	else: print("No dulplicated")


