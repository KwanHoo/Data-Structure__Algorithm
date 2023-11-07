# 1954_달팽이 숫자

## N*N 배열 숫자 시계방향

T = int(input())

for tc in range(T):
    N = int(input())

    # 리스트컴프리헨션
    data = [[0 for j in range(N)] for i in range(N)]
    
    dist = [[0,1],[1,0],[0,-1],[-1,0]]      # 우, 하, 좌, 상
    
    num = 1     #달팽이를 채울 숫자
    d = 0       #달팽이 이동방향 # 0:우, 1:하, 2:좌, 3:상 -> 시계방향 순서
    x, y = 0, -1    # 시작위치
    while num <= (N*N):
        nx, ny = x + dist[d][0], y + dist[d][1]
        if 0 <= nx < N and 0<= ny < N and data[nx][ny] == 0:
            data[nx][ny] = num # 숫자 넣는 부분
            num += 1 
            x, y = nx, ny   #현재 위치 갱신
            
            
            ## 달팽이 크기에서 벗어났거나, 해당 위치에 이미 숫자가 부여되어 있는 경우
            ## k값 조정을 통해 방향을 바꿈
        else:
            d = (d+1) %4    # 0, 1, 2, 3 으로만 움직일 수 있게 나머지를 구함
    
    print(f'#{tc+1}')
    for row in data:
        print(*row)
