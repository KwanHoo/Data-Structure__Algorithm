# 8741_두문자어

## 단어의 앞글자만 대문자 따로

T = int(input())

for tc in range(T):
    words = input()
    wL = len(words)

    resultl = ''
    first = words[0]
    resultl += first.upper()
    for i in range(wL):
        temp = words[i]
        if temp == ' ':
            nextw = words[i+1]

            # resultl.append(nextw)
            resultl = resultl + nextw.upper()

    print(f'#{tc+1} {resultl}')

# 파이썬 제출 안됨