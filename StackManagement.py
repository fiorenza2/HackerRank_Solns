# Check if brackets are is_matched
# Trick here was to 'return not stack' for empty lists ( was using if len == 0 , which is to slow )

def is_matched(expression):
    left = ['[','{','(']
    right = [']','}',')']

    l_dic = {}
    r_dic = {}

    for i,(l,r) in enumerate(zip(left,right)):
        l_dic[l] = i
        r_dic[r] = i

    stack = []

    for brack in expression:
        if brack in r_dic:
            if stack and l_dic[stack[-1]] == r_dic[brack]:
                stack.pop()
            else:
                return False
        else:
            stack.append(brack)
    return not stack


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
