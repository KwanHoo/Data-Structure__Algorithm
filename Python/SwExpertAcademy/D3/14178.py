# 14178_1차원 정원

# 1차원 수직선
# 모든 정수 i에 꽃이 하나씩 심겨 있음
# ex) N = 5 이면 1, 2, 3, 4, 5 이렇게 꽃이 심어져 잇는거
# 자동분무기 사용 : 분무기는 정수 좌표에 놓을 수 있음
## x에 분무기를 놓을 경우 닫힌 구간 [x-D, x+D]에 심긴 모든 꽃들에 물을 줄 수 있음

# 모든 꽃이 한 개 이상의 분무기에서 물을 받을 수 있도록 하기 위 해 필요한 최소한의 분무기수

T = int(input())

for tc in range(T):
    N, D = map(int, input().split())
    count = 1

    fir = 1+D*2 # 분무기 한개의 길이
    one_l = fir
    while one_l<N:
        if one_l == N:
            break
        else:
            count += 1
        one_l += fir            ## 루프시 분무기 한개의 값 더해주기!

    print(f'#{tc+1} {count}')