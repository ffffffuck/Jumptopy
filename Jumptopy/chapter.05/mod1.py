def sum(a,b):
    return a+b


def safe_sum(a,b):
    if type(a) != type(b):
        print("더할수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a,b)
    return result

if __name__ == " __main__":
    print(sum(1,2))
    print(safe_sum(2,'hello'))
