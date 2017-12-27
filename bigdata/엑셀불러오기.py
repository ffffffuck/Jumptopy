import csv

with open("C:\\Users\\user\\Desktop\\Demographic_Statistics_By_Zip_Code.csv", newline='') as infile:
    data = list(csv.reader(infile))

countParticipantsindex= data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS:" +str(countParticipantsindex))

countPartcipants=[]

for  cloumn in data[1:]:
    countPartcipants.append(int(cloumn[countParticipantsindex]))


print(countPartcipants)