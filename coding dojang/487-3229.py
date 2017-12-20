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


dic_a = list(dic)

# print(dic_a)

if 'ABC' in dic:
    print('true')
else: print('false')