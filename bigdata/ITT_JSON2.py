import json

with open('ITT_Student.json',encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)

def presentation(i):
    print("<<학생정보>>")
    print('ID:'+list(i.values())[3])
    print('이름:'+list(i.values())[4]) #이름
    print('나이:' + list(i.values())[2])
    print('주소:' + list(i.values())[1])
    print('과거 수강횟수:'+list(i['lecture_information'].values())[1])# 과거 수강횟수
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
        print('강의코드:'+list(j.values())[1])
        print('강의명:'+list(j.values())[2])
        print('강사:'+list(j.values())[4])
        print('개강일:' + list(j.values())[3])
        print('종강일:' + list(j.values())[0])
        print()


# a ='ITT001'
# #아이디로 찾기
# list_n=[]
# for i in data:
#     if a == list(i.values())[3]:
#         list_n.append(list(i.values())[3])
#     list_n = sorted(list(set(list_n)))
#     if len(list_n) > 1:
#         for f in list_n:
#             print(f)
#     else:
#         if a == list(i.values())[3]:
#             presentation(i)

#이름으로 찾기
a='김기정'
list_n=[]
for i in data:
    if a == list(i.values())[4]:
        list_n.append(list(i.values())[3])
    list_n = sorted(list(set(list_n)))
    if len(list_n) > 1:
        for f in list_n:
            print(f)
    else:
        if a == list(i.values())[4]:
            presentation(i)

#나이로 찾기
# a='31'
# list_n=[]
# for i in data:
#     if a == list(i.values())[2]:
#         list_n.append(list(i.values())[3])
#     list_n = sorted(list(set(list_n)))
#     if len(list_n) > 1:
#         for f in list_n:
#             print(f)
#     else:
#         if a == list(i.values())[2]:
#             presentation(i)

#주소로 찾기
# a = '대구광역시 달서구 성지로 14안길 17'
# list_n=[]
# for i in data:
#     if a == list(i.values())[1]:
#         list_n.append(list(i.values())[3])
#     list_n = sorted(list(set(list_n)))
#     if len(list_n) > 1:
#         for f in list_n:
#             print(f)
#     else:
#         if a == list(i.values())[1]:
#             presentation(i)

#수강횟수로 찾기
# a='1'
# list_n=[]
# for i in data:
#     if a == list(i['lecture_information'].values())[1]:
#         list_n.append(list(i.values())[3])
#     list_n = sorted(list(set(list_n)))
#     if len(list_n) > 1:
#         for f in list_n:
#             print(f)
#     else:
#         if a == list(i['lecture_information'].values())[1]:
#             presentation(i)




### 강의정보
#강의 이름으로 찾기
# a ='IoT 빅데이터 실무반'
# list_n=[]
# for i in data:
#     for j in list(list(i.values())[0].values())[0]:
#         if a ==list(j.values())[2]:
#             list_n.append(list(i.values())[3])
# list_n = sorted(list(set(list_n)))
# if len(list_n) > 1:
#     for f in list_n:
#         print(f)
# else:
#     for i in data:
#         for j in list(list(i.values())[0].values())[0]:
#             if a == list(j.values())[2]:
#                 lecture_presentaion(j)

#수강하는 학생명으로 찾기
# a='전수범'
# list_n=[]
# for i in data:
#     for j in list(list(i.values())[0].values())[0]:
#         if a ==list(i.values())[4]:
#             list_n.append(list(i.values())[3])
# list_n = sorted(list(set(list_n)))
# if len(list_n) > 1:
#     for f in list_n:
#         print(f)
# else:
#     for i in data:
#         for j in list(list(i.values())[0].values())[0]:
#             if a == list(i.values())[4]:
#                 lecture_presentaion(j)

#강사이름으로 찾기
# a = '이현구'
# list_n=[]
# for i in data:
#     for j in list(list(i.values())[0].values())[0]:
#         if a ==list(j.values())[4]:
#             list_n.append(list(i.values())[3])
# list_n = sorted(list(set(list_n)))
# if len(list_n) > 1:
#     for f in list_n:
#         print(f)
# else:
#     for i in data:
#         for j in list(list(i.values())[0].values())[0]:
#             if a == list(j.values())[4]:
#                 lecture_presentaion(j)


