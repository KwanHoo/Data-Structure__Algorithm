# 1940_가랏! RC카!

# 0: 현재 속도 유지
# 1: 가속
# 2: 감속

T = int(input())

for tc in range(T):
    N = int(input()) #커멘드 수
    result = 0  # 거리
    ns = 0  # 현재스피드
    for nc in range(N):
        temp = input()

        if len(temp) ==1:
            cm = 0
        else:
            cm = temp[0]
            sp = temp[2:]

        if int(cm) == 0:
            result += ns
        elif int(cm) == 1:
            ns += int(sp)
            result += ns
        elif int(cm) == 2:
            ns -= int(sp)
            if ns < 0:  # abs() 절댓값함수
                ns = 0
            result += ns

    print(f'#{tc+1} {result}')


