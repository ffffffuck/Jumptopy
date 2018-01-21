from bs4 import BeautifulSoup as bs
import requests

# 해당 페이지 회차번호 또는 추첨날짜를 추출하는 함수
def info(soup, tag):
    return soup.select('h3.result_title')[0].find(tag).get_text()

baseUrl = "http://nlotto.co.kr/gameResult.do?method=win520"
soup = bs(requests.get(baseUrl).content, 'html.parser')

recent = info(soup, 'strong')
print('연금복권 1등 당첨번호 찾기\n')
print('최근 %s' % info(soup, 'span'))
print('********%s회********\n' % recent)

while True:
    while True:
        try:
            lotto_round = int(input('회차를 입력하세요 : '))
            if lotto_round <0 or lotto_round> int(recent):
                print('\n해당 회차가 존재하지 않습니다')
                continue
            break
        except ValueError:
            print("\n숫자만 입력해야 합니다")

    lottoUrl = baseUrl + '&Round=' + str(lotto_round)
    soup = bs(requests.get(lottoUrl).content, 'html.parser')
    # 첫번째 번호
    no1_1 = soup.find("ul", class_="no1_1").select("li")
    no1_1 = [number.get_text(strip=True) for number in no1_1]
    # 두번째 번호
    no1_2 = soup.find("ul", class_="no1_2").select("li")
    no1_2 = [number.get_text(strip=True) for number in no1_2]

    print('\n%s회 당첨번호\n' % info(soup, 'strong'))
    print(info(soup, 'span')+'\n')
    print(' '.join(no1_1))
    print(' '.join(no1_2))

    a = input('\n다시 하려면 r 을 입력하세요 ')
    if a in ['r', 'R', 'ㄱ', 'ㄲ']:
        continue
    else:
        break