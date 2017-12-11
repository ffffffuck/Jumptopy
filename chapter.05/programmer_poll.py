list = ""
while True:
    a=input("프로그래밍이 왜 좋으세요?")
    if a == '종료': exit()
    b = input("이름이 어떻게 되세요?")
    print("설문에 응해주셔서 감사합니다")
    if b != '종료':
        list += ("["+b+"]" +" "+ a)+"\n"
    if b =='종료':
        print(list)
        try:
            f=open("poll.txt", "r+")
            f.write(list+"\n")
            f.close()
            exit()
        except:
            D = input("poll.txt 파일이 없습니다. 아래 중 선택하세요.\n1:종료\n2:변경된 파일경로 입력")
            if D == '1':
                print("종료합니다")
                exit()
            if D == '2':
                E=input("경로를 설정해주세요:")+"\poll.txt"
                print(E)
                f = open(E, 'a')
                f.write(list + "\n")
                f.close()
                print("저장되었습니다.")
                exit