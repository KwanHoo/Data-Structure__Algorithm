# 올바른 괄호

## 괄호 올바른지 판별
## 스택 이용
def solution(s):
    answer = True
    temp = []
    for i in s:
        if i == '(':
            temp.append(i) ## 스택에 넣기
        elif i == ')':
            if len(temp)==0: ## 스택에 없어 -> False
                return False
            else:
                temp.pop()
        # print(i, temp)
    # print(temp)
    if len(temp) != 0: ## 스택에 남아있어 -> False
        answer = False

    return answer