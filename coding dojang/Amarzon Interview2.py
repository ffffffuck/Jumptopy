def t2s(src):
    h, m, s = map(int, src.split(":"))
    return h*3600 + m*60 + s


def isBoundTime(com_time, out_time, chk_time):
    if  t2s( chk_time ) >= t2s( com_time ) and t2s( chk_time ) <= t2s( out_time ):
        return True
    else:
        return False

def countWorkers(chk_time):
    sum = 0
    for record in input:
        com_time, out_time = record.split(" ")
        if isBoundTime(com_time, out_time, chk_time):
            sum += 1
    return sum

input = [
'09:12:23 11:14:35',
'10:34:01 13:23:40',
'10:34:31 11:20:10'
]

#  ==  테스트  ===
print( "작업자수: {0}명".format(countWorkers("10:50:10")))
