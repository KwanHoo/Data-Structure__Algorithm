# 문제집) Python 배우기 (1~50)
## 1934_최소공배수
# 브론즈 1

## 유클리드 호제법 이용!!
T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    # result = 0

    # 최소공배수 계산
    result = A * B

    while B>0:
        A,B = B, A%B

    print(result//A)