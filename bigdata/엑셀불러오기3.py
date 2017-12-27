import csv

def get_csv_rowInstance(row_name):
    n_index=data[0].index(row_name)
    row_instance=[]
    for cloumn in data[1:]:
        row_instance.append(cloumn[n_index])
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
    name_list = get_csv_rowInstance("JURISDICTION NAME")
    n_index=name_list.index(str(col_instance))
    for i in data[n_index+1]:
        print(i)

with open("C:\\Users\\user\\Desktop\\Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data=list(csv.reader(infile))


# get_csv_rowInstance("PERCENT FEMALE")
print_row(get_csv_rowInstance("COUNT PARTICIPANTS"),'str')
print_col(10002)
