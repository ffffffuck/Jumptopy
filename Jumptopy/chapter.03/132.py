marks = [90,25,67,45,80]
number =0
for mark in marks:
    number +=1
    if mark < 60: continue
    print("%s번째 학생 합격입니다 축하합니다" %number)
