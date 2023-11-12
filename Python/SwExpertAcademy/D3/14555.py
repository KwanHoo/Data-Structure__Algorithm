# 14555_공과 잡초

# 1차원 초원 ....
# 열린 괄호 + 닫힌 괄호  () => 공
#! 서로 다른 두 공이 겹치지 않음
# | : 잡초 , 칸을 가리는 역할
## 초원에 놓았을 수 있는 공의 개수의 최솟값

#! 1이상50이하 S

## 최소 공이 되는 경우의 수
#1. ()
#1-2 (|
#2. |)

T = int(input())

for tc in range(T):
    S = list(map(str, input()))
    # print(S)

    count = 0

    for i in range(len(S)):
        if S[i] == '(':
            if i+1 != len(S):
                if S[i+1] == ')':
                    count +=1
                elif S[i+1] == '|':
                    count +=1
                else:
                    continue
        elif S[i] == '|':
            if i+1 != len(S):
                if S[i+1] == ')':
                    count += 1
                else:
                    continue
        else:
            continue
    print(f'#{tc+1} {count}')