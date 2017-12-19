input ='11:00:00'
log= '''
09:12:23 11:14:35
10:34:01 13:23:40
10:34:31 11:20:10
'''
log= log.split('\n')[1:-1]
n=0
cul=[]
teo=[]
teo2=[]
for i in log:
    cul.append(i.split(' ')[0])
    teo.append(i.split(' ')[1])
for i in teo:
    teo2.append(i.replace(str(i[:2]),str(int(i[:2])+12)))
for i in range(len(log)):
    if cul[i] <= input <= teo2[i]:
        n+=1
print("%s시에 %s명 남아있었습니다"%(input,n))


