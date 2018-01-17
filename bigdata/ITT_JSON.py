import json


data = []

try:
    with open('ITT_Student.json',encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        data = json.loads(json_string)
except:
    with open('ITT_Student.json','w', encoding='utf8') as outfile:
        readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        print('ITT_Student.json 을 읽습니다.')


student_Profile={}
lecture_content = {}
lecture_information = {}

student_Profile['student_id'] = 'ITT'+'{:0=3}'.format(len(data)+1)

student_Profile['student_name'],student_Profile['student_age'] = input("학생이름과 나이를 입력하세요:").split(' ')

student_Profile['student_adress'] = input("주소를 입력하세요:")

lecture_information['lecture_pre_record'] = input("과거 학원에서 수강한적이 있다면 횟수를 입력하세요:")

lecture_content['lecture_code'] = input("강의코드를 입력하세요:")

lecture_content['lecture_name'] = input("강의명을 입력하세요:")

lecture_content['lecture_teacher'] = input("강사를 입력하세요:")

lecture_content['lecture_open'] = input("개강일을 입력하세요:")

lecture_content['lecture_close'] = input("개강 종료일을 입력하세요:")

lecture_information['lecture_content'] = lecture_content

student_Profile['lecture_information'] = lecture_information

data.append(student_Profile)


with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
    readable_result = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(readable_result)
    print('ITT_Student.json SAVED')
