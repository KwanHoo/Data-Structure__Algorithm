# 문자열을 정수로 바꾸기
def solution(s):
    answer = 0

    if s[0] == '-':
        # 음수
        sliceS = s[1:]
        print(sliceS)
        answer = -1 * int(sliceS)
    else:
        answer = int(s)
    return answer
