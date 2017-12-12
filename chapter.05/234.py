print(abs(-3))

print(all([1,2,3]))

print(all([1,2,3,0]))

print(any([1,2,3,0]))

print(any([0,""]))


#chr
print(chr(98))

print(chr(48))

#dir

print(dir([1,2,3]))

print(dir({'1':'a'}))


#divmod

print(divmod(7,3))

print(divmod(1.3,0.2))

#enumerate

for i, name in enumerate(['body','foo','bar']):
    print(i,name)


#eval

print(eval('1+2'))

print(eval("'hi' + 'a'"))

print(eval('divmod(4,3)'))


#filter

def positive(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result

print(positive([1, -3, 2, 0, -5, 6]))


def positive(x):
    return x >0

print(list(filter(positive,[1,-3,2,0,-5,6])))

print(list(filter()))

