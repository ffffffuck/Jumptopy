import json
from bs4 import BeautifulSoup

with open('ITT_Student.json',encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)

def print_content(a,content):
    n = 0
    while True:
        if a == content:
            n=n+1
    if a == content:
        if n > 1 : print('ID:' + list(i.values())[3])
        else : lecture_presentaion(i)


def presentation(i):
    print('ID:'+list(i.values())[3])
    print('이름:'+list(i.values())[4]) #이름
    print('나이:' + list(i.values())[2])
    print('주소:' + list(i.values())[1])
    print('과거 수강횟수:'+list(i['lecture_information'].values())[1]) # 과거 수강횟수
    print('<<수강정보>>')
    print('강의코드:'+list(i.values())[3]) #강의코드
    print('강의명:'+list(list(list(i.values())[0].values())[0].values())[2])
    print('강사:'+list(list(list(i.values())[0].values())[0].values())[4])
    print('개강일:'+list(list(list(i.values())[0].values())[0].values())[3])
    print('종료일:'+list(list(list(i.values())[0].values())[0].values())[0])
    print()


def lecture_presentaion(i):
    print('<<수강정보>>')
    print('강의코드:' + list(i.values())[3])  # 강의코드
    print('강의명:' + list(list(list(i.values())[0].values())[0].values())[2])
    print('강사:' + list(list(list(i.values())[0].values())[0].values())[4])
    print('개강일:' + list(list(list(i.values())[0].values())[0].values())[3])
    print('종료일:' + list(list(list(i.values())[0].values())[0].values())[0])
    print()

for i in data:
    id = list(i.values())[3]
    name = list(i.values())[4]
    age = list(i.values())[2]
    adress = list(i.values())[1]
    pre_lec_num = list(i['lecture_information'].values())[1]
    lec_code = list(i.values())[3]
    lec_name = list(list(list(i.values())[0].values())[0].values())[2]
    lec_teacher = list(list(list(i.values())[0].values())[0].values())[4]
    lec_open = list(list(list(i.values())[0].values())[0].values())[3]
    lec_close = list(list(list(i.values())[0].values())[0].values())[0]



    a = 'IoT 빅데이터 실무반'
    print_content(a,lec_name)







# for i in data: #아이디
#     n=0
#     a  ='ITT003'
#     if a == list(i.values())[3]:
#         n += 1
#         if n > 1 : print('ID:'+list(i.values())[3])
#         else : presentation()
#
# for i in data:#이름
#     n=0
#     a = '김인한'
#     if a == list(i.values())[4]:
#         n += 1
#         if n > 1 : print('ID:' + list(i.values())[3])
#         else : presentation()
#
# for i in data: #주소
#     n=0
#     a = "대구시 동구 동대구역로"
#     if a ==list(i.values())[1]:
#         n += 1
#         if n > 1 : print('ID:' + list(i.values())[3])
#         else : presentation()
#
# for i in data: # 수강횟수
#     a = "0"
#     n=0
#     if list(i['lecture_information'].values())[1]:
#         n+=1
#         if n > 1 : print('ID:' + list(i.values())[3])
#         else : presentation()

# def lecture_student(data):
#     n=0
#     for i in data: # 강의를 수강하는 학생
#         a = '김인한'
#         if a ==list(i.values())[4]:
#             n+=1
#     for i in data:
#         if a == list(i.values())[4]:
#             if n > 1 : print('ID:' + list(i.values())[3])
#             else : lecture_presentaion(i)


# a = 'IoT 빅데이터 실무반'
# def lecture_name(data): #강의명으로 검색
#     n=0
#     for i in data:
#         # a = 'IoT 빅데이터 실무반'
#         if a == list(list(list(i.values())[0].values())[0].values())[2]:
#             n = n+1
#     for i in data:
#         if a == list(list(list(i.values())[0].values())[0].values())[2]:
#             if n > 1 : print('ID:' + list(i.values())[3])
#             else : lecture_presentaion(i)
#
#
# lecture_name(data)


