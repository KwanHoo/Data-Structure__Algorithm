# 짝지어 제거하기

## 스택이용 풀이

##* [] -> len()
##* stack.pop()  stack.append()
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        ## 짝지어 수행 가능
        return 1
    else:
        return 0
