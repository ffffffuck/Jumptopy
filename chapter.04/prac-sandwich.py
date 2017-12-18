def input_ingredient():
    while True:
        while a == 1 :
            b= input("\n안녕하세요 원하시는 재료를 입력하세요:")
            if b != '종료':
                f=open("ingredient_list.txt", 'a')
                f.write(b+'\n')
                f.close()
            if b == '종료':
                break
        if a == 2: print("\n감사합니다 다음에 이용해주세요\n")
        return

def make_sandwiches():
    if a != 2:
        print('샌드위치를 만들겠습니다.\n')
        f=open("ingredient_list.txt", 'r')
        lines=f.readlines()
        for line in lines:
            print(line[:-1]+' 추가합니다')
        print('\n여기 주문하신 샌드위치 만들었습니다 맛있게 드세요\n')
        f.close()
        f=open("ingredient_list.txt", 'a')
        f.close()

f=open("ingredient_list.txt", 'a')
while True:
    a= int(input("안녕하세요 저희 가게에 방문해 주셔서 감사합니다\n1.주문\n2.종료\n입력:"))
    input_ingredient()
    make_sandwiches()