print("프로그래머들을 상대로한 설문조사입니다. 응해주셔서 감사합니다.")
list = ""
while True:
    a=input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료):")
    if a != '종료':
        b = input("이름이 어떻게 되세요?:")
        list += ("["+b+"]" +" "+ a)+"\n"
        print("설문에 응해주셔서 감사합니다")
    if a =='종료':
        print(list)
        try:
            f=open("poll.txt", 'r')
            line = f.readlines()
            f.close()
            f=open("poll.txt", 'a')
            f.write(list)
            f.close()
            print("저장되었습니다.")
            break
        except:
            D = int(input("poll.txt 파일이 없습니다. 아래 중 선택하세요.\n1:종료\n2:변경된 파일경로 입력"))
            if D == 1:
                print("종료합니다")
                exit()
            elif D == 2:
                E=input("경로를 설정해주세요:")+"\poll.txt"
                print(E)
                f = open(E, 'a')
                f.write(list)
                f.close()
                print("저장되었습니다.")
                exit()