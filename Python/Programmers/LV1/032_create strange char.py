# 이상한 문자 만들기
def solution(s):
    answer = ''
    s = s.split(' ')
    # print(s)
    for word in s:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    # print(answer[:-1])
    # print(answer[:-1].rstrip())

    return answer[:-1]


def solution2(s):
    answer = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            if (i % 2) == 0:
                # 짝
                # answer += upper(s[i])
                answer += s[i].upper()
            else:
                # 홀
                answer += s[i].lower()

    return answer