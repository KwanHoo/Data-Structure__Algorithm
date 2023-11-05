# 1966_숫자를 정렬하자

# 주어진  N 길이의 숫자열을 올므차순으로 정렬하여 출력하라

# N : 5이상 50이하

T = int(input())

for tc in range(T):
    N = int(input())
    input_li = list(map(int, input().split()))

    # print(input)
    in_sort = sorted(input_li)

    print(f'#{tc+1}', end =" ")     # 뒤 개행 문자 수정
    print(*in_sort)

## 변수명 주의할것!! -> 런타임에러 발생
# TypeError: 'list' object is not callable
# - 함수와 변수명이 중복되었을 때 발생
# - 파이썬에서 쓰이는 함수를 변수명으로 선언한 뒤, 밑에서 그 함수를 호출하려고 하면 해당 에러가 발생