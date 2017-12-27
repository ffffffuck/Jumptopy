import csv

with open("C:\\Users\\user\\Desktop\\Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data=list(csv.reader(infile))

countcitizenstatustotalindex=data[0].index("COUNT CITIZEN STATUS TOTAL")
print("countcitizenstatustotalindex: %d" %countcitizenstatustotalindex)

countcitizenstatustotal=[]

for cloumn in data[1:]:
    countcitizenstatustotal.append(int(cloumn[countcitizenstatustotalindex]))

for i in countcitizenstatustotal:
    print(i)

