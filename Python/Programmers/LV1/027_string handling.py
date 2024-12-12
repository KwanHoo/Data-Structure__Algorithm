# 문자열 다루기 기본

# ! 숫자로만 구성되어야함!
# ! 문자열 길이는 4 or 6
def solution(s):
    answer = True

    # s = 4 or 6
    # print('0', ord('0'))    ## 0 : 48
    # print('9', ord('9'))    ## 9 : 57
    if len(s) == 4 or len(s) == 6:

        for i in range(len(s)):

            temp = s[i]
            t2 = ord(temp)
            # print('t2, temp : ', t2, temp)
            ## 숫자 조건 fail
            if (ord(temp) < 48) or (ord(temp) > 57):
                return False

    else:  ## 길이 조건 fail
        return False

    return answer