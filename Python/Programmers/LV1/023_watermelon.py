# 수박수박수박수박수박수?

def solution(n):
    answer = ''

    if (n % 2) == 0:
        # 짝
        answer = "수박" * (n // 2)
    else:
        # 홀
        answer = "수박" * (n // 2) + "수"
    return answer