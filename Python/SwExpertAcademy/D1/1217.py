# 1217_거듭제곱

T= 10
for tc in range(T):
    No = int(input())

    a, b = map(int, input().split())

    result = a**b

    print(f'#{No} {result}')