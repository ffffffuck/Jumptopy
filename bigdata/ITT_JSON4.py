import json

with open('ITT_Student.json',encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)

def presentation(i):
    print("<<학생정보>>")
    print('ID:' + list(i.values())[3])
    print('이름:' + list(i.values())[4])
    print('나이:' + list(i.values())[2])
    print('주소:' + list(i.values())[1])
    print('과거 수강횟수:' + list(i['lecture_information'].values())[1])  # 과거 수강횟수
    print()
    print('<<수강정보>>')
    for j in list(list(i.values())[0].values())[0]:
        print('강의코드:' + list(j.values())[1])
        print('강의명:' + list(j.values())[2])
        print('강사:' + list(j.values())[4])
        print('개강일:' + list(j.values())[3])
        print('강사:' + list(j.values())[0])
        print()


b = 'IB171106'
a = 'ITT002'
# a = input("삭제할 학생의 ID를 입력하세요:")
for i in range(len(data)):
    if a == data[i]['student_id']:
        data_index = data.index(data[i])
del data[data_index]

print(data)



# for i in range(len(data)):
#     if a == data[i]['student_id']:
#         for j in data[i]['lecture_information']['lecture_course']:
#             if b == j['lecture_code']:
#                 lec_index = data[i]['lecture_information']['lecture_course'].index(j)
#                 del  data[i]['lecture_information']['lecture_course'][lec_index]

