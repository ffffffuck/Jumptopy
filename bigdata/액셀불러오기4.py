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
            print(int(float(i)))
        elif type == 'float':
            print(float(i))
        elif type == 'str':
            print(str(i))

def print_col(col_instance):
    for i in data[col_instance]:
        print(i)

def get_csv_colInstance(primary_key):
    col_list=[]
    name_list = get_csv_rowInstance("JURISDICTION NAME")
    n_index=name_list.index(str(primary_key))
    for i in range(len(data[n_index+1])):
        col_list.append(data[n_index+1][i])
    return col_list

def print_colInstance(colInstance):
    for i in colInstance:
        print(i)


with open("C:\\Users\\user\\Desktop\\Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data=list(csv.reader(infile))

# get_csv_rowInstance("PERCENT FEMALE")
# print_row(get_csv_rowInstance("PERCENT FEMALE"),'int')
# print_col(1)
# get_csv_colInstance(10002)
# print_colInstance(get_csv_colInstance(10002))


while True:
    input1 = input("Access 데이터유형(1.행,2열,3,종료):")
    if input1 == '1':
        row_name= input("Access 키를 입력하세요:")
        print_row(get_csv_rowInstance(row_name),'str')
    elif input1 == '2':
        primary_key=input("Access 키를 입력하세요:")
        print_colInstance(get_csv_colInstance(int(primary_key)))
    elif input1 == '3':
        print("프로그램을 종료합니다.")
        break