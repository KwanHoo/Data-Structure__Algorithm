# JadenCase 문자열 만들기

## title() : 문장의 모든 단어의 첫 글자를 대문자로, 나머지는 소문자
## capitalize(): 문장의 첫 글자만 대문자로, 나머지는 소문자
def solution33(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i] = s[i].capitalize()
    answer = ' '.join(s)
    return answer


def solution(s):
    answer = []
    s = s.split(" ") ## 공백으로 단어 분리
    for word in s:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else: ## else인경우 word가 false인경우임.. -> 공백인건가??
            # print('else', word)
            answer.append(word)
    return " ".join(answer)


## 런타임에러 44
def solution2(s):
    answer = ''
    # numl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    temp = list(s.split(' '))
    # print(temp)
    temp2 = ""
    for i in temp:
        # if i[0] in numl:
        # temp2 += i
        # temp2 += " "
        # else:
        f = i[0].upper()
        if len(i) > 1:
            ft = f + i[1:].lower()
        else:
            ft = f
        temp2 += ft
        temp2 += " "
    # print(temp2)
    answer = temp2.strip()
    return answer


# 런타임 에러 44
def solution3(s):
    answer = ''
    numl = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    temp = list(s.split(' '))
    print(temp)
    temp2 = ""
    for i in temp:
        if i[0] in numl:
            temp2 += i
            temp2 += " "
        else:
            f = i[0].upper()
            if len(i) > 1:
                ft = f + i[1:].lower()
            else:
                ft = f
            temp2 += ft
            temp2 += " "
    print(temp2)
    answer = temp2.strip()

    return answer