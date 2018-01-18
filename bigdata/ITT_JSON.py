import json
import os

data = []

def save():
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print('ITT_Student.json SAVED\n')

def presentation(i):
    print("\n<<학생정보>>\n")
    print('ID:' + i['student_id'])
    print('이름:' + i['student_name'])
    print('나이:' + i['student_age'])
    print('주소:' + i['student_adress'])
    print('과거 수강횟수:'+i['lecture_information']['lecture_pre_record']+'\n')  # 과거 수강횟수
    for j in i['lecture_information']['lecture_course']:
        lecture_presentaion(j)

def lecture_presentaion(j):
    print('<<수강정보>>\n')
    print('강의코드:' + j['lecture_code'])
    print('강의명:' + j['lecture_name'])
    print('강사:' + j['lecture_teacher'])
    print('개강일:' + j['lecture_open'])
    print('종강일:' + j['lecture_close'])
    print()

def lec_print(what):
    list_n = []
    for i in data:
        for j in i['lecture_information']['lecture_course']:
            if a in j[what]:
                if len(a) == 1:
                    if a == j[what][0]:
                        list_n.append(i['student_id'])
                    else:
                        pass
                else:
                    list_n.append(i['student_id'])
    list_n = sorted(list(set(list_n)))
    if len(list_n) > 1:
        print("중복결과가 나왔음으로 ID만 출력합니다.\n")
        for f in list_n:
            print(f)
    elif len(list_n) == 1:
        for i in data:
            for j in i['lecture_information']['lecture_course']:
                if a in j[what]:
                    lecture_presentaion(j)

def student_print(what):
    list_n=[]
    for i in data:
        if what == 'lecture_pre_record':
            if a in i['lecture_information'][what] :
                if len(a) == 1:
                    if a == i['lecture_information'][what][0]:
                        list_n.append(i['student_id'])
                    else:pass
                else:
                    list_n.append(i['student_id'])
        else:
            if a in i[what]:
                if len(a) == 1:
                    if a == i[what][0]:
                        list_n.append(i['student_id'])
                    else:pass
                else:
                    list_n.append(i['student_id'])
    list_n = sorted(list(set(list_n)))
    if len(list_n) > 1:
        print("중복결과가 나왔음으로 ID만 출력합니다.\n")
        for f in list_n:
            print("       "+f)
    elif len(list_n) == 1:
        for i in data:
            if what == 'lecture_pre_record':
                if a in i['lecture_information'][what]:
                    presentation(i)
            else:
                if a in i[what]:
                    presentation(i)

################### 학생 수강정보 입력 #####################
while True:

    if os.path.isfile("ITT_Student.json"):
        with open('ITT_Student.json', encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            data = json.loads(json_string)
    else:
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)

    if os.path.isfile("id_index.txt"):
        with open("id_index.txt",'r')as infile:
            read_index = infile.readline()
    else:
        with open("id_index.txt",'w') as infile:
            infile.write(str(0))
        with open('id_index.txt','r')as infile:
            read_index = infile.readline()

    print('<< json기반 주소록 관리 프로그램 >>')
    print('1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료')
    inp = input('   입력:')
    if inp == '1':
        student_Profile={}
        lecture_course=[]
        lecture_content = {}
        lecture_information = {}

        student_Profile['student_id'] = 'ITT'+('{:0=3}'.format(int(read_index)+1))

        student_Profile['student_name'],student_Profile['student_age'] = input("\n학생이름과 나이를 입력하세요:").split(' ')

        student_Profile['student_adress'] = input("\n주소를 입력하세요:")

        lecture_information['lecture_pre_record'] = input("\n과거 학원에서 수강한적이 있다면 횟수를 입력하세요:")

        while True:
            lecture_content['lecture_code'] = input("\n강의코드를 입력하세요:")

            lecture_content['lecture_name'] = input("\n강의명을 입력하세요:")

            lecture_content['lecture_teacher'] = input("\n강사를 입력하세요:")

            lecture_content['lecture_open'] = input("\n개강일을 입력하세요:")

            lecture_content['lecture_close'] = input("\n종강일을 입력하세요:")

            lecture_course.append(lecture_content)

            lecture_information['lecture_course'] = lecture_course

            student_Profile['lecture_information'] = lecture_information

            lecture_content = {}
            print("1. 강의 추가 입력\n2. 뒤로가기")
            f = input("입력:")
            if f =='1': pass
            elif f == '2':break

        data.append(student_Profile)
        with open("id_index.txt", 'w') as infile:
            infile.write(str(int(read_index) + 1))
        save()

##################학생 수강정보 입력 ################
    elif inp =='2':
        print("\n<<학생 정보를 조회합니다>>\n")
        print('0. 전체학생정보 조회\n1. ID로 조회\n2. 이름으로 조회\n3. 나이로 조회\n4. 주소로 조회\n5. 과거 수강 횟수로 조회\n\n<<강의 정보를 조회합니다>>\n\n6. 학생명으로 강의조회\n7. 강의명으로 강의조회\n8. 강사명으로 강의조회\n9. 첫페이지로')
        jo = input("입력:")
        if jo =='0':
            for i in data:
                presentation(i)

        elif jo =='1':
            a = input("id를 입력하세요:")
            student_print('student_id')

        elif jo =='2':
            a = input("이름을 입력하세요:")
            student_print('student_name')

        elif jo =='3':
            a = input("나이를 입력하세요:")
            student_print('student_age')

        elif jo =='4':
            list_n=[]
            student_print('student_adress:')

        elif jo =='5':
            a = input("수강횟수를 입력하세요:")
            student_print('lecture_pre_record')

        elif jo =='6':
            a = input("학생이름을 입력하세요:")
            lec_print('student_id')

        elif jo =='7':
            a = input("강의명을 입력하세요:")
            lec_print('lecture_name')

        elif jo =='8':
            a = input("강사명을 입력하세요:")
            lec_print('lecture_teacher')

#################### 학생정보 수강정보 수정 하기 ######################################
    elif inp =='3':
        for i in data:
            presentation(i)
        a = input("수정할 학생의 id를 입력하세요(0입력시 첫페이지로):\n")
        if a == '0':
            continue
        else: pass
        for i in data:
            if a == list(i.values())[3]:
                print('수정할 정보를 선택하세요.\n1. 이름\n2. 나이\n3. 주소\n4. 과거 수강횟수')
                b=input('입력:')
                if b =='1':
                    i['student_name'] = input('변경할 이름을 입력하세요:')
                elif b == '2':
                    i['student_age'] = input('변경할 이름을 입력하세요:')
                elif b == '3':
                    i['student_adress'] = input('변경할 주소를 입력하세요:')
                elif b =='4':
                     i['lecture_information']['lecture_pre_record'] = input('변경할 수강횟수를 입력하세요:')
                print("변경되었습니다.")
                presentation(i)

        save()

######################## 학생정보 수강정보 삭제하기 #############################
    elif inp == '4':
        print("삭제할 요소를 선택하세요\n1. 학생정보\n2. 강의정보\n3. 첫페이지로")
        del_con = input("입력:")
        if del_con== '1':
            a = input("삭제할 학생의 ID를 입력하세요:")
            for i in data:
                if a == i['student_id']:
                    data_index = data.index(i)
                    del data[data_index]
            print("\n삭제 되었습니다.\n")
        elif del_con =='2':
            a = input("삭제할 강의를 가진 학생 ID를 입력하세요:")
            b = input("삭제할 강의코드를 입력하세요:")
            for i in data:
                if a == i['student_id']:
                    for j in i['lecture_information']['lecture_course']:
                        if b == j['lecture_code']:
                            lec_index = i['lecture_information']['lecture_course'].index(j)
                            del i['lecture_information']['lecture_course'][lec_index]
                            print("\n삭제되었습니다.\n")
        elif del_con =='3':
            continue

        save()

    elif inp == '5':
        exit()