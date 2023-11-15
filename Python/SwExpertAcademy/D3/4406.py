# 4406_모음이 보이지 않는 사람

#! 알파벳 소문자만으로 이루어진 단어 제시

# 모음 : a, e, i, o, u

T = int(input())

for tc in range(T):
    istr = list(map(str,input()))
    result = ''
    mo = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(istr)):
        temp = istr[i]

        if temp in mo:
            continue
        else:
            result += temp
    print(f'#{tc+1} {result}')