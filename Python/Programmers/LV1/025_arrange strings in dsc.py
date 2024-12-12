# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''

    s = list(s)
    s.sort()
    s.reverse()
    answer = "".join(s)
    return answer


def solution2(s):
    return ''.join(sorted(s, reverse=True))