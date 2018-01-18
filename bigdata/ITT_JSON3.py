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


def lecture_presentaion(j):
    print('<<수강정보>>')
    print('강의코드:' + list(j.values())[1])
    print('강의명:' + list(j.values())[2])
    print('강사:' + list(j.values())[4])
    print('개강일:' + list(j.values())[3])
    print('종강일:' + list(j.values())[0])
    print()


for i in data:
    presentation(i)
a = input("수정할 학생의 id를 입력하세요")
for i in data:
    if a ==list(i.values())[3]:
        b= input('수정할 정보를 선택하세요(1:이름 2:나이 3:주소 4:과거수강횟수')
        if b == '1':
            c= input('변경할 이름을 입력하세요:')
            i['student_name'] = c
            print()
            print('변경되었습니다.')
            print()
            presentation(i)
        elif b =='2':
            c = input('변경할 나이를 입력하세요:')
            i['student_age'] = c
            print()
            print('변경되었습니다.')
            print()
            presentation(i)
        elif b == '3':
            c = input('변경할 주소를 입력하세요:')
            i['student_adress'] = c
            print()
            print('변경되었습니다.')
            print()
            presentation(i)
        else:
            c = input('변경할 수강횟수를 입력하세요:')
            i['lecture_information']['lecture_pre_record']= c
            print()
            print('변경되었습니다.')
            print()
            presentation(i)

