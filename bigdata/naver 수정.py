import json

def rep(a):
    a = a.replace('&quot;', '\"')
    return a
a = "이상득 &quot;26일 예정대로 출석&quot; 검찰 통보…건강변수는 여전"
# a = a.replace('&quot;', '\"')

print(rep(a))
