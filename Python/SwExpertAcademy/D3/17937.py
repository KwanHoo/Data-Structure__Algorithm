# 17937_큰 수의 최대공약수

# 최대공약수 GCD(S) : S의 모든 원소를 나눌 수 있는 자연수 중 가장 큰 것
## ex) GCD({ 70, 105, 42}) = 7

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())

    if A == B:
        GCD = A
    else:
        GCD = 1

    print(f'#{tc+1} {GCD}')