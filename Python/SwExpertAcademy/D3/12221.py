# 12221_구구단2

# 석환이 1이상 9 이하의 자연수 두개를 곱셈할수는 있음 두자리수는 못함

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    result = 0
    if A > 9 or B > 9:
        result = -1
    else:
        result = A * B

    print(f'#{tc+1} {result}')