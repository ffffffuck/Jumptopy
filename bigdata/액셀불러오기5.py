import csv


def get_csv_rowInstance(row_name):
    n_index=data[0].index(row_name)
    row_instance=[]
    for row in data[1:]:
        row_instance.append(row[n_index])
    return row_instance

def print_row(row_instance, type='int'):
    for i in row_instance:
        if type == 'int':
            print(int(i),end=' ')
        elif type == 'float':
            print("%g" % float(i),end=' ')

def print_row2(row_instance, row_instance2, type='int'):
    for i in range(len(row_instance)):
        print(row_instance[i], "   ", "%0.2f" % row_instance2[i])

def get_csv_colInstance(primary_key):
    col_list = []
    name_list = get_csv_rowInstance("JURISDICTION NAME")
    n_index = name_list.index(str(primary_key))
    for i in range(len(data[n_index + 1])):
        col_list.append(data[n_index + 1][i])
    return col_list

def print_colInstance(colInstance):
    for i in colInstance:
        print(i, end=' ')

def type_check(data):
    try:
        list(map(int,data))
        return 'int'
    except:
        list(map(float,data))
        return 'float'

def my_sum(data):
    result = 0
    for i in data:
        result+=float(i)
    return float(result)

def my_avg(data):
    return my_sum(data)/len(data)

def my_max(data):
    return max(list(map(float,data)))

def my_min(data):
    return min(list(map(float,data)))

def my_dev(data):
    result=[]
    for i in data:
        result.append(float(i) - float(my_avg(data)))
    return result

def my_vari(data):
    result=0
    for i in my_dev(data):
        result+=pow(i,2)
    return float(result/len(data))

def my_stdev(data):
    return pow(my_vari(data),0.5)


with open("Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data=list(csv.reader(infile))

while True:
    input1=input("메뉴를 고르세요(1:총합 2:평균 3:최대값 4:최소값 5:편차 6:표준편차 7:분산 8:정렬 9:행 10:열 11:종료):")
    if input1 == '1':
        a=input("Header Cloumn을 입력하세요:")
        b=type_check(get_csv_rowInstance(a))
        print("요소들은:")
        print_row(get_csv_rowInstance(a),b)
        print()
        print("총합은:(sum(a))","%g" %my_sum(get_csv_rowInstance(a)))

    elif input1 =='2':
        a=input("Header Cloumn을 입력하세요:")
        b = type_check(get_csv_rowInstance(a))
        print("요소들은")
        print_row(get_csv_rowInstance(a),b)
        print()
        print("평균은:(sum(a)/len(a))","%g"%my_avg(get_csv_rowInstance(a)))

    elif input1 =='3':
        a = input("Header Cloumn을 입력하세요:")
        b = type_check(get_csv_rowInstance(a))
        print("요소들은")
        print_row(get_csv_rowInstance(a),b)
        print()
        print("최대값은:(max(a))","%g"%my_max(get_csv_rowInstance(a)))

    elif input1 == '4':
        a = input("Header Cloumn을 입력하세요:")
        b = type_check(get_csv_rowInstance(a))
        print("요소들은")
        print_row(get_csv_rowInstance(a),b)
        print()
        print("최소값은:(min(a))","%g"%my_min(get_csv_rowInstance(a)))

    elif input1 == '5':
        a = input("Header Cloumn을 입력하세요:")
        b = type_check(get_csv_rowInstance(a))
        print("요소와 편차는(표본-평균):")
        print_row2(get_csv_rowInstance(a),my_dev(get_csv_rowInstance(a)),b)
        print()

    elif input1 =='6':
        a= input("Header Cloumn을 입력하세요")
        b = type_check(get_csv_rowInstance(a))
        print("요소들은")
        print_row(get_csv_rowInstance(a),b)
        print()
        print("표준편차는:(√분산)")
        print("%0.2f" %my_stdev(get_csv_rowInstance(a)))
        print()

    elif input1 =='7':
        a= input("Header Cloumn을 입력하세요")
        b = type_check(get_csv_rowInstance(a))
        print("요소들은")
        print_row(get_csv_rowInstance(a),b)
        print()
        print("분산은:(∑(표본-평균)**/표본수)")
        print("%g" %my_vari(get_csv_rowInstance(a)))

    elif input1 =='8':
        a = input("Header Cloumn을 입력하세요")
        b = type_check(get_csv_rowInstance(a))
        c= input("1:내림차수 2:오름차수:")
        if c == '1':
            print_row(reversed(sorted(map(float, get_csv_rowInstance(a)))),b)
            print()
        elif c =='2':
            print_row(sorted(map(float, get_csv_rowInstance(a))),b)
            print()

    elif input1 =='9':
        a = input("Access키를 입력하세요:")
        print_row(get_csv_rowInstance(a),'str')

    elif input1 == '10':
        primary_key = input("Primary Key를 입력하세요:")
        print_colInstance(get_csv_colInstance(primary_key))

    elif input1 == '11':
        print("프로그램을 종료합니다.")
        break