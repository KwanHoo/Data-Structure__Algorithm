# 시저암호

#! 'z' 1만큼 밀면 'a'가 됨
def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        else:
            temp = ord(i)
            if (temp > 96 and temp < 123):
                # 소문자
                temp += n
                if (temp > 122):
                    temp -= 26

            elif (temp > 64 and temp < 91):
                # 대문자
                temp += n
                if (temp > 90):
                    temp -= 26

            temp2 = chr(temp)

            answer += temp2
    # print(answer)
    # print('a', ord('a')) # 97
    # print('z', ord('z')) # 122
    # print('A', ord('A')) # 65
    # print('Z', ord('Z')) # 90

    return answer