input='''
((((((())
()))
((((()))))
(()))(
())(()
(()((())()))
'''
def isBalanced(s):
    n=0
    for i in range(len(s)):
        if s[i]=='(':
            n+=1
        else : n-=1
        if n < 0:
            return False

    return True if n==0 else False

# print(isBalanced('(()()()())'))
# print(isBalanced('(((())))'))
# print(isBalanced('(()((())()))'))
# print(isBalanced('((((((())'))
print(isBalanced('())(()'))
# print(isBalanced('(()()(()'))
# print(isBalanced('(()))('))
