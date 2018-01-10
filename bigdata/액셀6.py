import csv

def find_Header(x):
    Header_file=[]
    Header = data[0].index(x)
    for i in data[1:]:
        Header_file.append(i[Header])
    return Header_file

def primary_key(x):
    key_list=find_Header("JURISDICTION NAME")
    a= key_list.index(x)
    return data[a+1]

def my_sum(x):
    result=0
    for i in x:
        result+=float(i)
    return result

def my_avg(x):
    return my_sum(x)/len(x)

def my_max(x):
    return max(map(float,x))

def my_min(x):
    return min(map(float,x))

def my_dev(x):
    for i in x:
        print("%0.2f"%float(i),'\t\t',"%g"%(float(i)-my_avg(x)))

def my_vari(x):
    vari_sum=0
    for i in x:
        vari_sum+=pow(float(i)-my_avg(x),2)
    return vari_sum/len(x)

def my_stdev(x):
    return pow(my_vari(x),0.5)

def array(x):
    return sorted(map(float,x))

def re_array(x):
    return reversed(sorted(map(float,x)))

def print_list(x):

    for i in x:
        if type(i) == int:
            print(int(i),end=' ')


with open("Demographic_Statistics_By_Zip_Code.csv") as infile:
    data = list(csv.reader(infile))

while True:
    a=input("1:행 2:열 3:최대값 4:최소값 5:평균 6:편차 7:표준편차 8:분산 9:정렬 10:총합 11:종료")
    if a=='1':
        x=input("Head Cloumn을 입력하세요")
        print("요소들은 :")
        print_list(find_Header(x))
        print()
    elif a=='2':
        x=input("Primary Key를 입력하세요")
        print("요소들은 :")
        print_list(primary_key(x))
        print()
    elif a=='3':
        x=input("Head Cloumn을 입력하세요")
        print("요소들은 :")
        print_list(find_Header(x))
        print()
        print("최대값은: %g"%my_max(find_Header(x)))
        print()
    elif a == '4':
        x = input("Head Cloumn을 입력하세요")
        print("요소들은 :")
        print_list(find_Header(x))
        print()
        print("최소값은: %g" % my_min(find_Header(x)))
        print()
    elif a == '5':
        x = input("Head Cloumn을 입력하세요")
        print("요소들은 :")
        print_list(find_Header(x))
        print()
        print("평균은: %g" % my_avg(find_Header(x)))
        print()
    elif a == '6':
        x = input("Head Cloumn을 입력하세요")
        print("표본과 편차는: ")
        my_dev(find_Header(x))
        print()
    elif a == '7':
        x = input("Head Cloumn을 입력하세요")
        print("요소들은 :")
        print_list(find_Header(x))
        print()
        print("표준편차는: %g" % my_stdev(find_Header(x)))
        print()
    elif a == '8':
        x = input("Head Cloumn을 입력하세요")
        print("요소들은 :")
        print_list(find_Header(x))
        print()
        print("분산은: %g" % my_vari(find_Header(x)))
        print()
    elif a == '9':
        b=input("1:내림차수 2:오름차수")
        if b =='1':
            x = input("Head Cloumn을 입력하세요")
            print_list(array(find_Header(x)))
            print()
        elif b =='2':
            x = input("HEad Cloumn을 입력하세요")
            print_list(re_array(find_Header(x)))
            print()
    elif a == '10':
        x = input("Head Cloumn을 입력하세요")
        print("요소들은 :")
        print_list(find_Header(x))
        print()
        print("총합은: %g" % print_list(my_sum(find_Header(x))))
        print()
    elif a =='11':
        print("프로그램을 종료합니다")
        break