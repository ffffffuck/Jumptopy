input = [5,8,2,4,6,1,3,7]
# input=(''.join(list(map(str,input))))

def sort(input):
    for i in range(1,len(input)):
        if input[i-1] > input[i]:
            if i+1 <= input[i]:
                input.insert(i+1, input[i-1])
                input.pop(i-1)
            else:
                input.insert(input[i]-1, input[i])
                input.pop(i+1)


            print(input)
sort(input)

