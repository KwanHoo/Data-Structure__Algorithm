# 알파벳을 숫자로 변환
# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환

## A -> 1, B -> 2, ... , Z -> 26 으로 변화

## sol)딕셔너리 활용

dic_str = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12,
           'M':13, 'N':14, 'O':15, 'P':16,
           'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

str_list = list(map(str, input().split())) # 입력이 문자열로 들어올거임
result_str = ''

for i in range(len(str_list[0])):
    temp = dic_str[str_list[0][i]]

    result_str = result_str + str(temp) + ' '  # int인거 스트링으로 형변환 해서 합치기
print(result_str)






