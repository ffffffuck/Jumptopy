n=0
while True:
    a = input("안녕하세요 이름을 입력하세요.:")
    n+=1
    if n == 1:
        s ='st'
    if n ==2:
        s ='nd'
    if n ==3:
        s ='rd'
    if n >=4 and n < 11:
        s = 'th'

    print("[%s]!! You are %s%s person come here!"%(a,n,s))
    if n >= 11:
        print("sorry [%s], The event is closed because You are %s%s person com here" %(a,n,s))


