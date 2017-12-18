
A= list(range(100,1000))
g=list(map(str, A))
g_list=[]
for i in g:
    if list(i)[2] != '0':
        g_list.append(i)
g_list=(list(map(int,g_list)))
a=[]
for x in g_list:
    b= str(x*int(str(x)[::-1]))
    a.append(b)
print(a)

# for i in range(len(a) - 1):
#     if int(a[i + 1]) - int(a[i]) < 0:
#         print(i)
#     else:
#         pass
