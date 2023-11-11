# 16910_원 안의 점

# 반지름 N 격자점의 개수

T = int(input())

for tc in range(T):
    N = int(input())

    # (0,0)점 한개 + 각 꼭짓점 4개 + x축 y축에 걸쳐있는 n-1개의 점 * 4(4분면)
    points = (N-1) * 4 + 5 #5(1+4)
    cnt = 0
    # print(points)

    # 한개의 분면 위에 조건에 맞는 점
    for i in range(1, N):
        for j in range(1, N):
            if (i**2) + (j**2) <= N**2:
                cnt += 1
    # print(cnt)
    points += (cnt*4)

    print(f'#{tc+1} {points}')