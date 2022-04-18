## 백준 8393
## 합
## [반복문], 구현, 수학

def suml(n):
    result = 0
    for i in range(1,n+1):
        result += i
    print(result)

if __name__ == "__main__":
    N = int(input())
    suml(N)


''' 참고 숏코드 가우스 공식
1 + 2 + ... + (n-1)+n = (n+1) * n / 2

n = int(input())
print(n*-~n//2)


~: 비트 반전 연산자
~x == -x - 1
-~x == x + 1
'''