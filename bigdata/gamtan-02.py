import csv
from pandas import DataFrame

with open("gamtan_수집데이터.csv",newline='')as infile:
    gamtan_list =list(csv.reader(infile))[1:]

result = []
result2 =[]
result3 =[]
location=[]
location_a= ''
for i in gamtan_list:
    location.append(i[0])

location = sorted(location)

n=1
for i in range(len(location)-1):
    if location[i] != location[i+1]:
        location_a=location_a+location[i]+','+str(n)+' '
        n=1
    else:n=n+1
location_a = location_a + location[i] +','+ str(n)+' '


location = location_a.split(' ')

for i in location[:-1]:
    loc=i.split(',')[0]
    num=i.split(',')[1]
    result.append([loc]+[num]+["%0.4f%%"%((int(num)/len(location))*10)])
    result2.append(int(num))
    # print(('%s지역은 전국 감탄매장중 %g%%의 매장이 입점해 있습니다' %(loc,(int(num)/len(location))*10)))
    # print()

result2.sort()
result2=list(reversed(result2))
for i in result2:
    for j in result:
        if str(i) in j:
            result3.append(j)
print(' ------------------------------ ')
print('|     지역     |지점수|    비율   |')
print(' ------------------------------ ')
for i in result3:
    # print(int(len(i[0])))
    if len(i[0]) ==3:
        space = '      '
    elif len(i[0]) ==5:
         space = '   '
    elif len(i[0]) == 4:
        space = '    '
    elif len(i[0]) == 7:
        space = ''
    # if len(i[1]) == 2:
    #     space2 = ' '
    print('| '+i[0]+space+' | '+i[1]+' | '+i[2]+' |')
    print(' ---------------------------- ')


# gamtan_table = DataFrame(result3, columns=("지역", "지점수", "비율"))
# gamtan_table.to_csv("gamtan_가공정보.csv", encoding='cp949', mode='w', index=False)


