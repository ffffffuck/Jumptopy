input = [5,2,4,6,1,3]

# input=(''.join(list(map(str,input))))

def sort(input):
    for i in range(1,len(input)):
        if input[i-1] > input[i]:
            if input.index(input[i]) <= input[i]:
                input.insert(input.index(input[i+1]), input[i-1])
                input.remove(input[i-1])
            else:
                input.insert(input[i], input[i-1])
                input.reverse()
                input. remove(input[i-1])
                input.reverse()
                print(input)
sort(input)