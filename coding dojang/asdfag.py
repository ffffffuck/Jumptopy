a = ""
N = (input("입력하세요"))
# N = "aaabbbcccaa"

# print(len(N[0:4]))
# print(N[0:2])
# N = N[3:]
# print(N)
# for i in range(len(N)):
#         if N[i] != N[i+1]:
#                 a = a + N[0] + str(len(N[0:i+1]))
#                 N = N[i:]

print(len(N[0:0]))
while i >= len(N):
        if N[i-1] != N[i]:
                print(i)
                print("조까")
                a = a+N[0]+str(len(N[0:i]))
                N = N[i:]
        print(a)

