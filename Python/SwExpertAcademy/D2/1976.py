# 1976_시각 덧셈

# 시분 2개 입력 받아 더한 값을 시분으로 출력

#! H : 1이상 12 이하 정수
#! M : 0이상 59 이하 정수

T = int(input())

for tt in range(T):
    H, M, h, m = map(int, input().split())

    time = 0
    minute = 0

    # 분 계산
    if M+m == 60 :
        minute = 0
    elif M+m > 60:
        minute = M+m - 60
        time += 1
    else:
        minute = M+m

    # 시간 계산
    temp = H + h + time
    if temp >12:
        time = temp -12
    else:
        time = temp

    print(f'#{tt+1} {time} {minute}')