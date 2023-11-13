# 13218_조별과제

# 월 수 수업
# 수강생 수 N
# 조 3명이상의 학생, 조의 수 최대화

T = int(input())

for tc in range(T):
    N = int(input())

    if N < 3:
        result = 0
    else:
        result = int(N // 3)

    print(f'#{tc+1} {result}')
