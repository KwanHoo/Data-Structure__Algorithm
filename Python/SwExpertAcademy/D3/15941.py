# 15941_평행사변형

# 모든 변의 길이가 N인 가장 넓은 평행사변형 => 정사각형

T = int(input())

for tc in range(T):
    N = int(input())

    result = N * N

    print(f'#{tc+1} {result}')