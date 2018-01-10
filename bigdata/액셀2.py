import csv

def row_Inst(x):
    result = []
    a = data[0].index(x)
    for i in data[1:]:
        result.append(i[a])
    return  list(map(float,result))

def cloumn_Inst(x):
    for i in data[1:]:
        if i[0] == x:
            return list(map(float,i))

def my_sum(x):
    result=0
    for i in x:
        result+=i
    return result

def my_avg(x):
    return my_sum(x)/len(x)

def my_max(x):
    return max(x)

def my_min(x):
    return min(x)

def my_dev(x):
    a = 0
    for i in x:
        if len("%g"%i)>a:
            a=len("%g"%i)
        space= ' '*(a-len("%g" %i))
        print("%g"%i+space+'\t\t'+(str("%g" %(i-my_avg(x))) if i-my_avg(x) < 0 else " "+str("%g" %(i-my_avg(x)))))

def my_vari(x):
    result=0
    for i in x:
        result+= pow(i-my_avg(x),2)
    return result/len(x)

def my_stdev(x):
    return pow(my_vari(x),0.5)

def array(x):
    return sorted(x)

def re_array(x):
    return reversed(array(x))

def print_list(x):
    try:
        for i in x:
            print("%g"%i, end=' ')
    except:print("%g"%x)


with open("Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data = list(csv.reader(infile))

while True:
    print()
    a= input("메뉴를 고르세요(1:행 2:열 3:총합 4:평균 5:최대값 6:최소값 7:편차 8:표준편차 9:분산 10:정렬 11:종료):")
    if a !='2' and a !='11':
        x = input("Headcloumn을 입력하세요:")
        if a !='10' and a !='7':
            print("요소들을 출력합니다.")
            print_list(row_Inst(x))

    if a =='1':
            continue

    elif a =='2':
        x=input("Primary key를 입력하세요:")
        print("요소들을 출력합니다.")
        print_list(cloumn_Inst(x))

    elif a =='3':
        print('\n'+"총합은:",end='')
        print_list(my_sum(row_Inst(x)))

    elif a =='4':
        print('\n'+"평균은:",end='')
        print_list(my_avg(row_Inst(x)))

    elif a =='5':
        print('\n'+"최대값은:",end='')
        print_list(my_max(row_Inst(x)))

    elif a =='6':
        print('\n'+"최소값은:",end='')
        print_list(my_min(row_Inst(x)))

    elif a =='7':
        print('\n'+"요소와 그 편차는:")
        my_dev(row_Inst(x))

    elif a =='8':
        print('\n'+"표준편차는:",end='')
        print_list(my_stdev(row_Inst(x)))

    elif a =='9':
        print('\n'+"분산은:",end='')
        print_list(my_vari(row_Inst(x)))

    elif a =='10':
        a = input("1: 내림차수 2:오름차수")
        if a =='1':
            print("내림차수 정렬:")
            print_list(re_array(row_Inst(x)))
        elif a =='2':
            print("오름차수 정렬:")
            print_list(array(row_Inst(x)))

    elif a =='11':
            print("프로그램을 종료합니다")
            break