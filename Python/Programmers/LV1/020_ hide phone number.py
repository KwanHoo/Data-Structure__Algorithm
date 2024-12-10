# 핸드폰 번호 가리기

## 1) 슬라이싱
## 2) for 반복하며 전반적으로
def solution(phone_number):
    answer = ''
    mn = len(phone_number) - 4
    temp = phone_number[:-4]
    temp2 = phone_number[-4:]

    tl = len(temp)
    answer = tl * '*' + temp2
    return answer