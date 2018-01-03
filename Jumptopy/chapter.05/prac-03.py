def check_number(input_number):
    if input_number % 10 == 0:
        return True
    else:
        return False

while True:
    input_number = int(input("양수를 입력하세요:"))
    if input_number == -1 :
        print("종료합니다")
        break
    else:
        print(check_number(input_number))
