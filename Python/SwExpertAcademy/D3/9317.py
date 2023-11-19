# 9317_석찬이의 받아쓰기

## 석찬이 받아쓰기 연습
# 몇개의 문자를 올바르게 적었는지 세어보자

T = int(input())

for tc in range(T):
    N = int(input())
    wright = list(map(str, input()))
    long = list(map(str, input()))

    good = 0

    for i in range(N):

        if wright[i] == long[i]:
            good +=1

    print(f'#{tc+1} {good}')

# python 제출 불가