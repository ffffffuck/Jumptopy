import json
import os

def save():
    f = input("1. 저장후 종료 \n2. 저장하지 않고 프로그램 종료")
    if f == '1':
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
            print('\n[ITT_Student.json]이 저장되었습니다.\n')
            exit("종료합니다.")
    if f =='2':
        exit('\n종료합니다.')

def index(data):
    id_index =[]
    for i in data:
        try:id_index.append(int(i['student_id'][3:]))
        except: id_index.append(0)
    for i in range(1,1000):
        if i not in sorted(id_index):
            student_Profile['student_id'] = 'ITT' + ('{:0=3}'.format(i))
            break

def presentation(i):
    print("\n<<<<<< 학생정보 >>>>>>\n")
    print('-ID:' + i['student_id'])
    print('-이름:' + i['student_name'])
    print('-나이:' + i['student_age'])
    print('-주소:' + i['student_adress'])
    print('-과거 수강횟수:'+i['lecture_information']['lecture_pre_record']+'\n')  # 과거 수강횟수
    for j in i['lecture_information']['lecture_course']:
        lecture_presentaion(j)

def lecture_presentaion(j):
    print('[수강정보]')
    print('.강의코드:' + j['lecture_code'])
    print('.강의명:' + j['lecture_name'])
    print('.강사:' + j['lecture_teacher'])
    print('.개강일:' + j['lecture_open'])
    print('.종강일:' + j['lecture_close']+'\n')

def part_search(list_n,i,what):
    if a in what:
        if len(a) == 1:
            if a == what[0]:list_n.append(i['student_name']+i['student_id'])
            else:pass
        else:list_n.append(i['student_name']+i['student_id'])
        return list_n

def print_id(list_n):
    if len(list_n) > 1:
        print("중복결과가 나왔음으로 ID만 출력합니다.\n")
        for f in list_n:
            print("ID : "+f[f.index('I'):]+"  이름 : "+f[:f.index('I')])

def lec_print(what):
    list_n = []
    for i in data:
        if what == 'student_name':
            part_search(list_n,i,i[what])
        else:
            for j in i['lecture_information']['lecture_course']:
                part_search(list_n,i,j[what])
    list_n = sorted(list(set(list_n)))
    print_id(list_n)
    if len(list_n) == 1:
        for i in data:
            for j in i['lecture_information']['lecture_course']:
                if what == 'student_name':
                    if a in i[what]:
                        lecture_presentaion(j)
                else:
                    if a in j[what]:
                        lecture_presentaion(j)

def student_print(what):
    list_n=[]
    for i in data:
        if what == 'lecture_pre_record':
            part_search(list_n,i,i['lecture_information'][what])

        else:part_search(list_n,i,i[what])
    list_n = sorted(list(set(list_n)))
    print_id(list_n)
    if len(list_n) == 1:
        for i in data:
            if what == 'lecture_pre_record':
                if a in i['lecture_information'][what]:
                    presentation(i)
            else:
                if a in i[what]:
                    presentation(i)

def fix(what):
    print('정말 수정하시겠습니까?(y/n)')
    f = input("입력 : ")
    if f == 'y':
        if 'lecture' in what:
            j[what] = a
        else: i[what] = a
        print("수정되었습니다.")
    elif f =='n':
        print("수정을 취소합니다.")


################### 학생 수강정보 입력 #####################
data = []
while True:
    if os.path.isfile("ITT_Student.json"):
        with open('ITT_Student.json', encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            data = json.loads(json_string)
            break
    else:
        f = input("파일이 없습니다.\n1. 경로 입력하기\n2. 현재 경로에 파일생성하기\n입력 : ")
        if f == '1':
            directory = input("경로를 입력하세요:")
            try:
                with open(directory + '\ITT_Student.json', encoding='UTF8') as json_file:
                    json_object = json.load(json_file)
                    json_string = json.dumps(json_object)
                    data = json.loads(json_string)
                    break
            except:
                print("옳은경로를 입력하세요.")
                continue
        elif f == '2':
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
        else:
            print("옳은값을 입력하세요:")
            continue

while True:
    print('<< json기반 주소록 관리 프로그램 >>')
    print('1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생 정보삭제\n5. 프로그램 종료')
    inp = input('입력 : ')
    if inp == '1':
        student_Profile={}
        lecture_course=[]
        lecture_content = {}
        lecture_information = {}

        student_Profile['student_name'] = input("\n이름을 입력하세요(ex:이창현,김인한..) : ")

        student_Profile['student_age'] = input("\n나이를 입력하세요:(ex:28,31,32..) : ")

        student_Profile['student_adress'] = input("\n주소를 입력하세요(ex:대구시 남구 대명동...) :")

        lecture_information['lecture_pre_record'] = input("\n과거 학원에서 수강한적이 있다면 횟수를 입력하세요(ex:0,3...) : ")

        f = '0'
        while True:
            lecture_content['lecture_code'] = input("\n강의코드를 입력하세요(ex:IB171106,OB171106) : ")

            lecture_content['lecture_name'] = input("\n강의명을 입력하세요(ex:IoT 빅데이터실무반, 오픈소스기반 빅데이터 실무반...) : ")

            lecture_content['lecture_teacher'] = input("\n강사를 입력하세요(ex:이현구) : ")

            lecture_content['lecture_open'] = input("\n개강일을 입력하세요(ex:2017-11-06) : ")

            lecture_content['lecture_close'] = input("\n종강일을 입력하세요(ex:2018-9-05) : ")

            lecture_course.append(lecture_content)

            lecture_information['lecture_course'] = lecture_course

            student_Profile['lecture_information'] = lecture_information

            lecture_content = {}

            print("\n1. 강의 추가 입력\n2. <저장> 후 뒤로가기\n3. 뒤로가기")
            f = input("입력 : ")
            if f =='1':
                continue
            elif f == '2':
                data.append(student_Profile)
                index(data)
                break
            elif f =='3':
                lecture_content = {}
                f ='2'
                break
            else:
                print("옳은 값을 입력하세요.\n")

        if f =='2':
            continue

##################학생 수강정보 입력 ################
    if inp == '2':
        jo='0'
        while True:
            print("\n<<학생 정보를 조회합니다>>\n")
            print('1. 전체학생정보 조회\n2. ID로 조회\n3. 이름으로 조회\n4. 나이로 조회\n5. 주소로 조회\n6. 과거 수강 횟수로 조회\n\n<<강의 정보를 조회합니다>>\n\n7. 학생명으로 강의조회\n8. 강의명으로 강의조회\n9. 강사명으로 강의조회\n10. 첫페이지로')
            jo = input("입력 : ")
            if jo =='1':
                for i in data:
                    presentation(i)

            elif jo =='2':
                a = input("id를 입력하세요:")
                student_print('student_id')

            elif jo =='3':
                a = input("이름을 입력하세요:")
                student_print('student_name')

            elif jo =='4':
                a = input("나이를 입력하세요:")
                student_print('student_age')

            elif jo =='5':
                a = input("주소를 입력하세요:")
                student_print('student_adress')

            elif jo =='6':
                a = input("수강횟수를 입력하세요:")
                student_print('lecture_pre_record')

            elif jo =='7':
                a = input("학생이름을 입력하세요:")
                lec_print('student_name')

            elif jo =='8':
                a = input("강의명을 입력하세요:")
                lec_print('lecture_name')

            elif jo =='9':
                a = input("강사명을 입력하세요:")
                lec_print('lecture_teacher')
            elif jo =='10':
                break
            else:
                print("옳은값을 입력하세요.")
                continue
        if jo =='10':
            continue

#################### 학생정보 수강정보 수정 하기 ######################################
    if inp =='3':
        a = '1'
        f ='y'
        j = '0'
        while True:
            b= '0'
            a = input("\n수정할 학생의 id를 입력하세요(0입력시 첫화면으로)\n입력 : ")
            if a == '0':break
            elif a in list(i['student_id'] for i in data):
                pass
            else:
                print("\n옳은값을 입력하세요.")
                continue

            for i in data:
                if a == i['student_id']:
                    presentation(i)
                    print('\n수정할 정보를 선택하세요.\n\n1. 학생 이름\n2. 학생 나이\n3. 학생 주소\n4. 학생 과거 수강횟수\n5. 강의 추가\n6. 강의 코드\n7. 강의 이름\n8. 강사명\n9. 개강일\n10. 종강일\n11. 뒤로가기')
                    b=input('\n입력:')
                    if b =='1':
                        a = input('변경할 이름을 입력하세요:')
                        fix('student_name')
                        pass

                    elif b == '2':
                        a= input('변경할 나이를 입력하세요:')
                        fix('student_age')
                        pass

                    elif b == '3':
                        a = input('변경할 주소를 입력하세요:')
                        fix('student_adress')
                        pass

                    elif b == '4':
                        a = input('변경할 수강횟수를 입력하세요:')
                        print('정말 수정하시겠습니까?(y/n)')
                        f = input("입력")
                        if f == 'y':
                            i['lecture_information']['lecture_pre_record'] = a
                            print("수정되었습니다.")
                            pass

                    elif b =='5':
                        lecture_content = {}

                        lecture_content['lecture_code'] = input("\n강의코드를 입력하세요(ex:IB171106,OB171106):\n")

                        lecture_content['lecture_name'] = input("\n강의명을 입력하세요(ex:IoT 빅데이터실무반, 오픈소스기반 빅데이터 실무반...):\n")

                        lecture_content['lecture_teacher'] = input("\n강사를 입력하세요(ex:이현구):\n")

                        lecture_content['lecture_open'] = input("\n개강일을 입력하세요(ex:2017-11-06):\n")

                        lecture_content['lecture_close'] = input("\n종강일을 입력하세요(ex:2018-9-05):\n")

                        i['lecture_information']['lecture_course'].append(lecture_content)

                    elif b =='6':
                        for j in i['lecture_information']['lecture_course']:
                            a = input("변경할 강의코드를 입력하세요")
                            fix('lecture_code')
                            break

                    elif b =='7':
                        for j in i['lecture_information']['lecture_course']:
                            a = input("변경할 강의이름를 입력하세요")
                            fix('lecture_name')
                            break

                    elif b =='8':
                        for j in i['lecture_information']['lecture_course']:
                            a = input("변경할 강사명를 입력하세요")
                            fix('lecture_teacher')
                            break

                    elif b =='9':
                        for j in i['lecture_information']['lecture_course']:
                            a = input("변경할 개강일 입력하세요")
                            fix('lecture_open')
                            break

                    elif b =='10':
                        for j in i['lecture_information']['lecture_course']:
                            a = input("변경할 종강일을 입력하세요")
                            fix('lecture_close')
                            break

                    elif b == '11':
                        break

                    else:
                        print("\n옳은값을 입력하세요.")
                        continue

                    print("1. 첫화면으로 2.더 수정하기")
                    j = input('입력:')
                    if j == '1':
                        break
            if j =='1':
                break
            if b =='11':
                break
        if a =='0':
            continue

######################## 학생정보 수강정보 삭제하기 #############################
    elif inp == '4':
        del_con=0
        while True:
            print("\n삭제할 요소를 선택하세요\n\n1. 학생정보\n2. 강의정보\n3. 첫페이지로")
            del_con = input("입력:")
            deldel = 'y'
            if del_con== '1':
                a = input("삭제할 학생의 ID를 입력하세요:")
                for i in data:
                    if a == i['student_id']:
                        data_index = data.index(i)
                        presentation(i)
                        print("정말 삭제하시겠습니까?(y/n)")
                        deldel = input('입력:')
                        if deldel == 'y':
                            del data[data_index]
                            print("\n삭제 되었습니다.\n")
                            break
                        elif deldel == 'n':
                            break
                if deldel == 'n':
                    continue

            if del_con =='2':
                a = input("삭제할 강의를 수강중인 학생 ID를 입력하세요:")
                if a in list(i['student_id'] for i in data):
                    pass
                else:
                    print("\n옳은값을 입력하세요")

                for i in data:
                    if a == i['student_id']:
                        presentation(i)
                        b = input("삭제할 강의코드를 입력하세요:")
                        for j in i['lecture_information']['lecture_course']:
                            if b == j['lecture_code']:
                                lec_index = i['lecture_information']['lecture_course'].index(j)
                                lecture_presentaion(j)
                                print("정말 삭제하시겠습니까?(y/n)")
                                deldel = input("입력:")
                                if deldel == 'y':
                                    del i['lecture_information']['lecture_course'][lec_index]
                                    print("\n삭제되었습니다.\n")
                                    break
                                elif deldel =='n':
                                    break

                if deldel =='n':
                    continue
            elif del_con =='3':
                break
            else:
                print('\n옳은값을 입력하세요')
                continue
        if del_con =='3':
            continue
    elif inp == '5':
        save()
        exit("\n종료합니다.")
    else:print("\n옳은값을 입력하세요.")