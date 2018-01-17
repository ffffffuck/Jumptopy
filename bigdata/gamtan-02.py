import csv
from pandas import DataFrame
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


with open("gamtan_수집데이터.csv",newline='')as infile:
    gamtan_list =list(csv.reader(infile))[1:]

result = []
num_list =[]
loc_list =[]
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
    loc_list.append(loc)
    num_list.append(int(num))

for i in range(len(loc_list)):
    result.append([loc_list[i]]+[str(num_list[i])]+['%0.2f%%'%((int(num_list[i])/sum(num_list))*100)])

num_list= list(reversed(sorted(set(num_list))))

for i in num_list:
    for j in result:
        if str(i) in j:
            result3.append(j)

# print(' ------------------------------ ')
# print('|     지역     |지점수|    비율   |')
# print(' ------------------------------ ')
# for i in result3:
#     print('| '+'%-13s|'%i[0])
#     print(' ------------------------------ ')
#
#
gamtan_table = DataFrame(result3, columns=("지역", "지점수", "비율"))
gamtan_table.to_csv("gamtan_가공정보.csv", encoding='cp949', mode='w', index=False)

# df=pd.read_csv("gamtan_가공정보.csv",encoding='euc-kr')


ax = gamtan_table.plot(kind='bar', title='지점통계', figsize=(12,4), legend=True, fontsize=12)

ax.set_xlabel('지역', fontsize=12)
ax.set_ylabel('지점수', fonsize=12)
ax.legend(['지점수'], fontsize=12)

# plt.show()