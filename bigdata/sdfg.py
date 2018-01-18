import json
import os

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
        lecture_presentaion(j)

def lecture_presentaion(j):
    print('강의코드:' + list(j.values())[1])
    print('강의명:' + list(j.values())[2])
    print('강사:' + list(j.values())[4])
    print('개강일:' + list(j.values())[3])
    print('종강일:' + list(j.values())[0])
    print()

def print_aa(what):
    list_n=[]
    if a in what:
        if len(a) ==1:
            if a == what[0]:
                list_n.append(list(i.values())[3])
            else:pass
        else:list_n.append(list(i.values())[3])
    return list_n

def fix(what):
    what = c
    print()
    print('변경되었습니다.')
    print()
    presentation(i)


def save():
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print('ITT_Student.json SAVED')

data = []

try:
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        data = json.loads(json_string)
except:
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        print('ITT_Student.json 을 읽습니다.')

################### 학생 수강정보 입력 #####################
while True:
    print('<< json기반 주소록 관리 프로그램 >>')
    inp = input('1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료')
    if inp == '1':
        student_Profile={}
        lecture_course=[]
        lecture_content = {}
        lecture_information = {}

        if os.path.isfile("id_index.txt"):
            with open("id_index.txt",'r')as infile:
                read_index = infile.readline()
        else:
            with open("id_index.txt",'w') as infile:
                infile.write(str(0))
            with open('id_index.txt','r')as infile:
                read_index = infile.readline()


        student_Profile['student_id'] = 'ITT'+('{:0=3}'.format(int(read_index)+1))

        student_Profile['student_name'],student_Profile['student_age'] = input("학생이름과 나이를 입력하세요:").split(' ')

        student_Profile['student_adress'] = input("주소를 입력하세요:")

        lecture_information['lecture_pre_record'] = input("과거 학원에서 수강한적이 있다면 횟수를 입력하세요:")

        while True:
            lecture_content['lecture_code'] = input("강의코드를 입력하세요:")

            lecture_content['lecture_name'] = input("강의명을 입력하세요:")

            lecture_content['lecture_teacher'] = input("강사를 입력하세요:")

            lecture_content['lecture_open'] = input("개강일을 입력하세요:")

            lecture_content['lecture_close'] = input("종강일을 입력하세요:")

            lecture_course.append(lecture_content)

            lecture_information['lecture_course'] = lecture_course

            student_Profile['lecture_information'] = lecture_information

            lecture_content = {}

            f = input("1:강의 더 입력하기 2:종료")
            if f =='1': pass
            if f =='2':break

        data.append(student_Profile)
        with open("id_index.txt", 'w') as infile:
            infile.write(str(int(read_index) + 1))
        save()


##################학생 수강정보 입력 ################

    elif inp =='2':
        print("\n<<학생 정보를 조회합니다>>\n")
        jo = input('0. 전체학생정보 조회\n1. ID로 조회\n2. 이름으로 조회\n3. 나이로 조회\n4. 주소로 조회\n5. 과거수강 횟수로 조회\n\n<<강의 정보를 조회합니다>>\n\n6. 학생명으로 강의조회\n7. 강의명으로 강의조회\n8. 강사명으로 강의조회\n9. 첫페이지로')
        if jo =='0':
            for i in data:
                presentation(i)

        elif jo =='1':
            list_n=[]
            a = input("id를 입력하세요")
            for i in data:
                list_n+=print_aa(list(i.values())[3])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n :
                    print(f)
            elif len(list_n) == 1:
                for i in data:
                    if a in list(i.values())[3]:
                        presentation(i)

        elif jo =='2':
            list_n=[]
            a = input("이름을 입력하세요")
            for i in data:
                list_n+=print_aa(list(i.values())[4])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n :
                    print(f)
            elif len(list_n) == 1:
                for i in data:
                    if a in list(i.values())[4]:
                        presentation(i)

        elif jo =='3':
            list_n=[]
            a = input("나이를 입력하세요")
            for i in data:
                list_n+=print_aa(list(i.values())[2])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n :
                    print(f)
            elif len(list_n) == 1:
                for i in data:
                    if a in list(i.values())[2]:
                        presentation(i)

        elif jo =='4':
            a = input("주소를 입력하세요:")
            list_n=[]
            for i in data:
                list_n+=print_aa(list(i.values())[1])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n :
                    print(f)
            elif len(list_n) == 1:
                for i in data:
                    if a in list(i.values())[1]:
                        presentation(i)

        elif jo =='5':
            a = input("수강횟수를 입력하세요:")
            list_n=[]
            for i in data:
                list_n += print_aa(list(i['lecture_information'].values())[1])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n:
                    print(f)
            elif len(list_n) == 1:
                for i in data:
                    if a == list(i['lecture_information'].values())[1]:
                        presentation(i)

        elif jo =='6':
            a = input("학생이름을 입력하세요:")
            list_n=[]
            for i in data:
                list_n += print_aa(list(i.values())[4])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n:
                    print(f)
            else:
                for i in data:
                    for j in list(list(i.values())[0].values())[0]:
                        if a in list(i.values())[4]:
                            lecture_presentaion(j)

        elif jo =='7':
            a = input("강의명을 입력하세요:")
            list_n=[]
            for i in data:
                for j in list(list(i.values())[0].values())[0]:
                    list_n += print_aa(list(j.values())[2])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n:
                    print(f)
            else:
                for i in data:
                    for j in list(list(i.values())[0].values())[0]:
                        if a in list(j.values())[2]:
                            lecture_presentaion(j)

        elif jo =='8':
            a = input("강사명을 입력하세요:")
            list_n=[]
            for i in data:
                for j in list(list(i.values())[0].values())[0]:
                    list_n += print_aa(list(j.values())[4])
            list_n = sorted(list(set(list_n)))
            if len(list_n) > 1:
                for f in list_n:
                    print(f)
            else:
                for i in data:
                    for j in list(list(i.values())[0].values())[0]:
                        if a in list(j.values())[4]:
                            lecture_presentaion(j)

#################### 학생정보 수강정보 수정 하기 ######################################

    elif inp =='3':
        for i in data:
            presentation(i)
        a = input("수정할 학생의 id를 입력하세요(0입력시 첫페이지로)")
        for i in data:
            if a == list(i.values())[3]:
                b = input('수정할 정보를 선택하세요(1:이름 2:나이 3:주소 4:과거수강횟수:')
                if b == '1':
                    c = input('변경할 이름을 입력하세요:')
                    i['student_name'] = c
                elif b == '2':
                    c = input('변경할 나이를 입력하세요:')
                    fix(i['student_age'])
                elif b == '3':
                    c = input('변경할 주소를 입력하세요:')
                    fix(i['student_adress'])
                elif b =='4':
                    c = input('변경할 수강횟수를 입력하세요:')
                    fix(i['lecture_information']['lecture_pre_record'])
            elif a == '0':
                pass

        save()

######################## 학생정보 수강정보 삭제하기 #############################

    elif inp == '4':
        del_con = input("삭제할 요소를 선택하세요(1:학생정보 2:강의정보 3:첫페이지로):")
        if del_con== '1':
            a = input("삭제할 학생의 ID를 입력하세요:")
            for i in range(len(data)):
                if a == data[i]['student_id']:
                    data_index = data.index(data[i])
            del data[data_index]
            print()
            print("삭제 되었습니다.")
        elif del_con =='2':
            a = input("삭제할 강의를 가진 학생 ID를 입력하세요:")
            b = input("삭제할 강의코드를 입력하세요:")
            for i in range(len(data)):
                if a == data[i]['student_id']:
                    for j in data[i]['lecture_information']['lecture_course']:
                        if b == j['lecture_code']:
                            lec_index = data[i]['lecture_information']['lecture_course'].index(j)
                            del data[i]['lecture_information']['lecture_course'][lec_index]
                            print()
                            print("삭제되었습니다.")

        save()

    elif inp == '5':
        exit()