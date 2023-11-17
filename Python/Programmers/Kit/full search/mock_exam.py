# 알고리즘 고득점 KIT _ 완전탐색
# 모의고사

# 수포자 1 : 12345 12345
# 수포자 2 : 21232425 21232425
# 수포자 3 : 3311224455 3311224455

N = list(map(int, input().split()))

def solution(answers):
    su1 = '12345'
    su2 = '21232425'
    su3 = '3311224455'

    su1A = ''
    su2A = ''
    su3A = ''
    c=0

    # 찍는 방식으로 답지 생성
    while c != len(answers):
        c1 = c % 5
        c2 = c % 8
        c3 = c % 10
        su1A = su1A + su1[c1]
        su2A = su2A + su2[c2]
        su3A = su3A + su3[c3]

        c += 1

    c1 = 0
    c2 = 0
    c3 = 0

    ## 정답과 일치 카운팅 부분
    for i in range(len(answers)):
        if int(su1A[i]) == answers[i]:
            c1 += 1
        if int(su2A[i]) == answers[i]:
            c2 += 1
        if int(su3A[i]) == answers[i]:
            c3 += 1

    maxc = max(c1, c2, c3)

    answer = []

    # 가장 높은 점수 받은 사람
    if c1 == maxc:
        answer.append(1)
    if c2 == maxc:
        answer.append(2)
    if c3 == maxc:
        answer.append(3)
    return answer


solution(N)
