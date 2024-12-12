# 가운데 글자 가져오기

## 홀수, 짝수 분기
def solution(s):
    answer = ''
    mid = 0

    if (len(s) % 2) != 0:
        # odd
        mid = len(s) // 2

        answer = s[mid]
    else:
        # even
        mid = len(s) // 2 - 1

        answer = s[mid:mid + 2]

    return answer