
def show_list():
    f= open("연습생.txt",'r')
    lines = f.readlines()
    for line in lines:
        print(line,end='')
    print()
    f.close()
    return

def make_idol():
    f=open("연습생.txt", 'r')
    lines = f.readlines()
    for line in lines[:-1]:
        print("신예 아이돌",line[:-1], "인기급상승")
    for line in lines[-1:]:
        print("신예 아이돌", line, "인기급상승")
    f.close()
    return

def make_world_star():
    f=open("연습생.txt", 'r')
    lines = f.readlines()
    for line in lines[:-1]:
        print("아이돌", line[:-1], "월드스타 등극")
    for line in lines[-1:]:
        print("아이돌", line, "월드스타 등극")
    f.close()
    return


show_list()
make_idol()
make_world_star()

